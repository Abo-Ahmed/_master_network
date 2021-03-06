
# colab link
# https://colab.research.google.com/drive/1QA3ufl7lur76WzBhuwerLdyjLj-8hoHC?authuser=2
# https://colab.research.google.com/notebooks/pro.ipynb

print(">>> main module loaded ...")
execfile('/content/_master/handler/handler.py')
# mount , details , project path
handler.intial_config(True, True, '/content/_master')
# path ,width , height , batchSize , startBatch , isColored
handler.dataset_config(handler.ePath, 100, 100, 30, 1, True)

handler.read_real()
# handler.read_sample( None)

# # handler.run_models(["CnnSeq"      , "CnnFunctional" , "ResNet" , "Vgg16"  , "vgg16Seq" ,
# #                     "VggLstm"     , "LstmConv2d"    , "Lstm"   , "LstmBi" , "VggBiLstm" ] )
# handler.special_run("VggBiLstm","program_1")
handler.special_run("AlexNet","program_1")

handler.final_config()
