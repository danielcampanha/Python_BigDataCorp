## Read Me ##
## This code we have a specific object of Kind of Information, and the code below check if we have duplicate objects in same configuration ##
## DbManager is the other file that is responsible to make the connection of Database ##

from DbManager import DbManager
from iteration_utilities import unique_everseen

all_groups = DbManager.get_all_groupsconfig()

groups_checked = 0

print('Groups Qty:' + str(len(all_groups)))

for group in all_groups:
    if group['Name'] == 'TESTE':
        a = 1

    group_id = group['_id']
    print('Checking group:' + group['Name'] + 'in Domain:' + group['Domain'])

    infotype_configs_list = group['InfoTypeConfigurations']
    question_config_list = group['QuestionsConfigurations']

    # remove duplicates from the infotypes_configurations
    corrected_infotypes = list(unique_everseen(infotype_configs_list))
    for infotype in corrected_infotypes:
        infotype_name = infotype['TypeName']
        duplicated_infotypes = list(filter(lambda x: x['TypeName'] == infotype_name, corrected_infotypes))
        if len(duplicated_infotypes) > 1:
            for i, duplicated in enumerate(duplicated_infotypes):
                if i != (len(duplicated_infotypes) - 1):
                    corrected_infotypes.remove(duplicated)

    # remove duplicates from the questions_configurations
    corrected_questions = list(unique_everseen(question_config_list))
    for question in corrected_questions:
        question_id = str(question['QuestionId'])
        duplicated_questions = list(filter(lambda x: x['QuestionId'] == question_id, corrected_questions))
        if len(duplicated_questions) > 1:
            for i, duplicated in enumerate(duplicated_questions):
                if i != (len(duplicated_questions) - 1):
                    corrected_questions.remove(duplicated)

    groups_checked += 1

    DbManager.update_group_config(group_id, corrected_questions, corrected_infotypes)

    print('Checked =' + str(id))
    print('GroupsChecked:' + str(groups_checked) + '/' + str(len(all_groups)))
