import os
import numpy as np
import shutil

def get_custom_folders(root_dir,target_dir='processed_data',transform_train=None, transform_val=None):
# # Creating Train / Val / Test folders (One time use)
    classes = os.listdir(root_dir+'/labeled/train')
    #c1 = classes[0]
    #c2 = classes[1]

    if os.path.exists(target_dir):
        shutil.rmtree(target_dir)
        os.makedirs(target_dir)

    # Creating partitions of the data after shuffeling
    for each_class in classes:
        currentCls = each_class
        train_src = root_dir+'/labeled/train/'+currentCls # Folder to copy images from
        

        allFileNames = os.listdir(train_src)
        np.random.shuffle(allFileNames)
        train_FileNames, val_FileNames = np.split(np.array(allFileNames),
                                                                [int(len(allFileNames)*0.9)])#, int(len(allFileNames)*0.85)])
        # train_FileNames, val_FileNames, test_FileNames = np.split(np.array(allFileNames),
        #                                                         [int(len(allFileNames)*0.7), int(len(allFileNames)*0.85)])


        train_FileNames = [train_src+'/'+ name for name in train_FileNames.tolist()]
        val_FileNames = [train_src+'/' + name for name in val_FileNames.tolist()]
        #test_FileNames = [train_src+'/' + name for name in test_FileNames.tolist()]

        test_src = root_dir+'/labeled/test/'+currentCls # Folder to copy images from
        test_allFileNames = os.listdir(test_src)
        # np.random.shuffle(allFileNames)

        
        print('Class : ', each_class)
        print('Total images: ', len(allFileNames))
        print('Training: ', len(train_FileNames))
        print('Validation: ', len(val_FileNames))
        #print('Testing: ', len(test_FileNames))
        
        test_allFileNames = [test_src+'/'+ name for name in test_allFileNames]
        print('Total Test images: ', len(test_allFileNames))
        tar = target_dir+'/test/'+currentCls # Folder to copy images to
        os.makedirs(tar)
        for f in test_allFileNames:
            shutil.copy(f, tar)
        print('\n')



        tar = target_dir+'/train/'+currentCls # Folder to copy images to
        os.makedirs(tar)
        for f in train_FileNames:
            shutil.copy(f, tar)

        tar = target_dir+'/val/'+currentCls # Folder to copy images to
        os.makedirs(tar)
        for f in val_FileNames:
            shutil.copy(f, tar)

        # tar = target_dir+'/test/'+currentCls # Folder to copy images to
        # os.makedirs(tar)
        # for f in test_FileNames:
        #     shutil.copy(f, tar)
    
    train_src = root_dir+'/unlabeled'
    allFileNames = os.listdir(train_src)
    # np.random.shuffle(allFileNames)
    
    allFileNames = [train_src+'/'+ name for name in allFileNames]
    print('Total Unlabeled images: ', len(allFileNames))
    print('\n')
    tar = target_dir+'/unlabeled/img' # Folder to copy images to
    os.makedirs(tar)
    for f in allFileNames:
        shutil.copy(f, tar)
    return target_dir

