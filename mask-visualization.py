
# coding: utf-8



import os
import os.path as osp
import json
#from labelme import utils
import warnings
import numpy as np
import cv2




def out_class(file_path, save_path, image_path=file_path):
    list1 = os.listdir(file_path) # 返回指定的文件夹包含的文件的名字列表
    json_list = []
    #jpg_list = []
    namelist = []
    for name in list1:
        #print(name)
        index = name.rfind('.')
        first_name = name[:index]
        tail_name = name[index:]
        #print(name2)
        #listName.append(name1)
        #print(listName)

        if tail_name == '.json':
            json_list.append(name)
            namelist.append(first_name) 
        #else:
            #jpg_list.append(name)
    #print(json_list)



    n=[0]
    print("当前正在处理的标签及文件：")
    for i in range(0, len(json_list)):
        json_path = os.path.join(file_path, json_list[i]) # 拼接出每个json文件的完整路径
        filename = os.path.basename(json_path)
        index = filename.rfind('.')
        first_name = filename[:index]
        
        #index = json_path.rfind('.')
        #first_name = json_path[:index]
                
        jpg_alln = first_name + '.jpg'
        jpg_path = os.path.join(image_path, jpg_alln)
        
        print("正在处理的图像为：")
        print(json_path)
        print(jpg_path)
        if os.path.isfile(json_path):
            #print(list1[i])
            data = json.load(open(json_path)) # 将json读取到data

            L1 = len(data['shapes']) # 每张图片的标签数量
            # print(i)
            for j in range(0, L1):

                #print('image label name: ', data['shapes'][j]['label'])
                point= (data['shapes'][j]['points'])
                #print(l)
                point = np.array(point)
                x=point[:,0]
                y=point[:,1]
                x_min = int(min(x))
                x_max = int(max(x))
                y_min = int(min(y))
                y_max = int(max(y))
                #print(x_min,x_max,y_min, y_max)
                
                img = cv2.imread(jpg_path)
                img = img[y_min:y_max, x_min:x_max]
                """
                给出输出文件路径
                """
                outpath = os.path.join(save_path, '%s' % data['shapes'][j]['label'])
                #print(outpath)
                exit = os.path.exists(outpath)
                #print((save_path， '/%s'% data['shapes'][j]['label']))
                                      #data['shapes'][j]['label']))

                if exit:
                    def check_meta(file_name):
                        """
                        给出输出文件路径
                        """

                        file_name_new=file_name
                        if os.path.isfile(file_name):
                            file_name_new=file_name[:file_name.rfind('.')]+'_'+str(n[0])+file_name[file_name.rfind('.'):]
                            n[0]+=1


                        if os.path.isfile(file_name_new):
                            file_name_new=check_meta(file_name)
                        return file_name_new
                    file_name  = os.path.join(outpath, '%s' % jpg_alln)
                    #file_name = ("./data_1/%s/%s.jpg" % (data['shapes'][j]['label'],listName[i]))
                    return_name=check_meta(file_name)

                    #print(return_name)

                    cv2.imwrite("%s"% return_name, img)
                else:
                    """
                    给出输出文件路径
                    """
                    os.makedirs(outpath)
                    file_name  = os.path.join(outpath, '%s' % jpg_alln)
                    cv2.imwrite((file_name), img)
    
    return 0

                    
if __name__ == '__main__':
    file_path = '/home/Data/lirenfu/tangshan20190404'
    save_path = '/home/Data/lirenfu/out_mask'
    image_path = '/home/Data/lirenfu/tangshan20190404'
    out_class(file_path, save_path, image_path)




