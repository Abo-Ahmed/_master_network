
class folder:
    @staticmethod
    def init_path():
        pass

    @staticmethod
    def get_file_count():
        return len(handler.fileList)

    @staticmethod
    def update_list():
        files = os.listdir(handler.dataPath)
        return files

    @staticmethod
    def is_exist(x):
        if str(x)+".jpg" in handler.fileList:
            return True
        else:
            return False

    @staticmethod
    def get_dir_image_num(x):
        x = str(x)
        if(len(x) <= 3):
            return int(x) , 0
        else:
            return int(x[-3:]) , int(x[:-3]) 

    @staticmethod
    def get_dir_image_name(folder_num , file_num):
        folder_num = str(folder_num)
        file_num = str(file_num)

        if(len(folder_num) == 1 ):
            folder_num = "00" + folder_num
        if(len(folder_num) == 2 ):
            folder_num = "0" + folder_num

        return "0"+folder_num , str(int(file_num + folder_num))

    @staticmethod
    def download_image( fd , fl):
        try:
            folderName , imageName = folder.get_dir_image_name(fd,fl)
            os.system('rsync rsync://176.9.41.242:873/danbooru2020/original/' + folderName + '/' + imageName + '.jpg ' + handler.dataPath)
        except Exception as e:
            print("XXX failed to download " + fd + " , " + fl  , folderName , imageName , e)

    @staticmethod
    def download_patch():
        handler.file = os.listdir(handler.dataPath)
        counter = 0
        for item in questionable.values:
            if str(item)+".jpg" in handler.file :
                counter += 1
                continue
            fd , fl = folder.get_dir_image_num(item)
            folder.download_image(fd, fl)
            print("counter " + str(counter) + " --> " + str(item))
            counter += 1
