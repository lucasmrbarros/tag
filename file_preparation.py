with open('datasets/projects.txt', 'r') as projects_file:
    projects_requirements = projects_file.readlines()
    projects_requirements_dict = {}

    projects_requirements_aux_list = []


    for i in range(len(projects_requirements)):
        aux_list = []

        if(i < 9):
            vacancy = projects_requirements[i][5]
            grades = projects_requirements[i][8]
        else:
            vacancy = projects_requirements[i][6]
            grades = projects_requirements[i][9]

        vacancy = int(vacancy)
        aux_list.append(vacancy)


        grades = int(grades)
        aux_list.append(grades)

        projects_requirements_aux_list.append(aux_list)
        projects_requirements_dict[i + 1] = projects_requirements_aux_list[i]

with open('datasets/studants.txt', 'r') as studants_file:
    studants = studants_file.readlines()
    studants_dict = {}

    studants_aux_list = []

    for i in range(len(studants)):
        begin_mark = False

        aux_studant = studants[i]

        len_aux_studants = len(aux_studant)

        aux_list = []

        for j in range(len_aux_studants):
            if aux_studant[j] == ':':
                begin_mark = True
                number = ''

            if begin_mark is True:
                if aux_studant[j] != ' ' and aux_studant[j] != 'P' and aux_studant[j] != '(' and aux_studant[j] != ')' and aux_studant[j] != ',' and aux_studant[j] != ':':
                    number = number + aux_studant[j]

                if(aux_studant[j] == ',') or (j + 5 == len_aux_studants):
                    number_to_int = int(number)
                    aux_list.append(number_to_int)
                    number = ''
                elif j + 1 == len_aux_studants:
                    number_to_int = int(number)
                    aux_list.append(number_to_int)
                    number = ''
        studants_dict[i + 1] = aux_list




