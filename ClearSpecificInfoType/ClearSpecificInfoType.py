
## Read Me ##
## This file is responsible for delete an especific kind of information of Group Configuration ##

from DbManager import DbManager

all_groups = DbManager.get_all_groupsconfig()

# InfoType that will be deleted.
infotype = {
            "TypeName" : "MOTHER_NAME",
            "Mandatory" : False,
            "Frequency" : 1
            }


Object_58 = {
            "QuestionId" : "58",
            "PositiveWeight" : 5,
            "NegativeWeight" : 0,
            "Frequency" : 1,
            "Enabled" : True,
            "AllowNoAAsCorrectAnswer" : False,
            "Mandatory" : False
            }

Object_59 = {
            "QuestionId" : "59",
            "PositiveWeight" : 5,
            "NegativeWeight" : 0,
            "Frequency" : 1,
            "Enabled" : True,
            "AllowNoAAsCorrectAnswer" : False,
            "Mandatory" : False
            }


i = 0
j = 0
k = 0
l = 0
infotype_config = [infotype]

for group in all_groups:
    id = group['_id']

    infotype_configs = group['InfoTypeConfigurations']    
    questions_configs = group['QuestionsConfigurations']
    if infotype in infotype_configs:        
        # Count of GroupConfiguration Updated
        i+=1
        infotype_configs.remove(infotype) 
    else:
        # Count of GroupConfigurations Not Updated
        j+=1
        continue   

    if (question_58 in questions_configs) and (question_59 in questions_configs):
        # Count of GroupConfiguration Updated
        k+=1
        questions_configs.remove(question_58)
        questions_configs.remove(question_59)        
    else:
        # Count of GroupConfigurations Not Updated
        l+=1
        continue

    DbManager.update_group_config(id, questions_configs, infotype_configs)
    
print('Updated =' + str(i))
print('NOT Updated =' + str(j))
