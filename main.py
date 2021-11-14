
# colab link
# https://colab.research.google.com/drive/1weN1Kz-UcRYYFSnYW5ABB0RX77npMmWO?authuser=2#scrollTo=63C7VVdMx0wa
print(">>> main module loaded ...")
execfile('/content/_master/handler/handler.py')
handler.intial_configurations(True , True , '/content/_master') # mount , details , project path

# loading and preparing dataset images
handler.read_data(None , 512 , 512) # datapath , width , height

# handler.runModels(["cnnFunctional" , "cnnSeq" ,   "res" , 
#                     "vgg16" , "vgg16seq", "vggLstm",
#                      "conv2Dlstm" , "lstm" , "lstmBi"])

handler.special_run("conv2Dlstm","program_0")
# handler.runModel("cnnFunctional","program_0") # model , program

handler.final_configurations()
