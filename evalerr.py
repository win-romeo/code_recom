#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sys,os
import subprocess

import sys


# In[12]:


TEST_DIR = '/home/wtemp/585/error/Test_Dataset/'

HOLE = "PREDICTION_HOLE_PLACEHOLDER"

PRED_DIR = "/home/wtemp/585/error/Predicted_Results/"
result_dict={}


# In[46]:


def write_result(path, res):
    with open(path, 'a+') as f:
        f.write(res)

def sample(s):
    return "None"


# In[47]:


# Param: the eval function
def test(eval_func):
    TEST_DIR = '/home/wtemp/585/error/Test_Dataset/'

    HOLE = "PREDICTION_HOLE_PLACEHOLDER"

    PRED_DIR = "/home/wtemp/585/error/Predicted_Results/"
    result_dict={}
    
    
    count = 0
    compiled = 0
    correct = 0
    for file in os.listdir(TEST_DIR):
        count += 1
#         print(count)
        if("test_sample" in file and "original" in file):
            continue
        if(file==".ipynb_checkpoints"):
            continue
        if("pycache" in file):
            continue

        # Read file
#         print("Openning "+TEST_DIR+file)
        f = open(TEST_DIR+file)
        context = f.read()
        seen = context.split(HOLE)[0]
        prediction = "x"

        if(HOLE not in context):
            print(file," has no hole to predict")
            continue
        if(context.count(HOLE)>1): # test data only contain 1 hole now, change later
            continue

        prediction = eval_func(seen)

        result = context.replace(HOLE, prediction)
        result_filename = file.replace(".", eval_func.__name__+".")
        write_result(PRED_DIR+result_filename,result)

        # Test result
        process = subprocess.Popen(["python", PRED_DIR+result_filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout = str(process.communicate())
        result_dict[TEST_DIR+file] = stdout

        if "SyntaxError" not in stdout:
            compiled += 1
            if "Error" not in stdout:
                correct += 1
                print(stdout)
    return count, compiled, correct


# In[48]:


#test(sample)
# result_dict


# In[ ]:
