# dc motor self excited series

from random import *
from sympy import *
import numpy as nm

def dcmotor2(difficulty_level):

    # Symbols


    R_f = Symbol('R_f')
    V_t = Symbol('V_t')
    E_a = Symbol('E_a')
    R_a = Symbol('R_a')
    I_a = Symbol('I_a')
    N = Symbol('N')
    phi = Symbol('\\phi')
    z = Symbol('z')
    P = Symbol('P')
    a = Symbol('a')
    K_a = Symbol('K_a')  # K_a * phi may have to be one unit
    T_e = Symbol('T_e')
    T_shaft = Symbol('T_shaft')
    omega_m = Symbol('\\omega_m')
    eff = Symbol('\\eta')
    P_losses = Symbol('P_losses')
    P_output = Symbol('P_output')
    P_fw = Symbol('P_F\\&W')
    I_path = Symbol('I_path')
    j = 1j

    # Equations
    e1 = ([V_t, I_a, R_f, E_a, R_a], Eq(V_t, (I_a*(R_a+R_f))+E_a), 'e1')
    e2 = ([E_a, phi, N, z, P, a], Eq(E_a, (phi*N*z*P)/(60*a)), 'e2')
    e3 = ([E_a, I_a, T_e, omega_m], Eq(E_a, (T_e*omega_m)/I_a), 'e3')
    e4 = ([T_e, K_a, phi, I_a], Eq(T_e, K_a*phi*I_a), 'e4')
    e5 = ([E_a, K_a, phi, omega_m], Eq(E_a, K_a*phi*omega_m), 'e5')
    e6 = ([K_a, z, P, a], Eq(K_a, (z*P)/(2*pi*a)), 'e6')
    e7 = ([omega_m, N], Eq(omega_m, (2*pi*N)/60), 'e7')
    e8 = ([eff, P_output, P_losses], Eq(eff, (P_output/(P_output+P_losses))*100), 'e8')
    e9 = ([P_losses, I_a, R_a, R_f, P_fw], Eq(P_losses, (((I_a**2)*(R_a+R_f))+P_fw)), 'e9')
    e10 = ([P_output, E_a, I_a, P_fw], Eq(P_output, (E_a*I_a)-P_fw), 'e10')
    e11 = ([P_output, T_e, omega_m, P_fw], Eq(P_output, (T_e*omega_m)-P_fw), 'e11')
    e12 = ([T_shaft, P_output, omega_m], Eq(T_shaft, P_output/omega_m), 'e12')
    e13 = ([I_path, I_a, a], Eq(I_path, I_a/a), 'e13')

    list_of_equations = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10,
                         e11, e12, e13]

    dict_of_equations = {'e1': e1, 'e2': e2, 'e3': e3, 'e4': e4, 'e5': e5,
                         'e6': e6, 'e7': e7, 'e8': e8, 'e9': e9,
                         'e10': e10, 'e11': e11,
                         'e12': e12,  'e13': e13}

    list_of_variables = [R_f, V_t, E_a, I_a, R_a, N, phi, z, P
                         , a, K_a, T_e, omega_m, eff, P_losses, P_output
                         , P_fw, T_shaft, I_path]

    always_known = [a, P]

    # ^ this must be a list of independent variables

    #NB f was removed from the list

    dict_of_var_names = {R_f: 'Field Resistance',
                         V_t: 'Terminal Voltage',
                         E_a: 'Induced EMF',
                         I_a: 'Armature Current',
                         R_a: 'Armature Resistance',
                         N: 'Rotational Speed of Armature (RPM)',
                         phi: 'Flux Per Pole',
                         z: 'Total Number of Active Conductors on the Armature',
                         P: 'Number of Poles',
                         a: 'Number of Parallel Paths in the Armature Winding',
                         K_a: 'Armature Constant',
                         T_e: 'Electromagnetic Torque',
                         T_shaft: 'Shaft Torque',
                         omega_m: 'Rotational Speed of Armature (rad/s)',
                         eff: 'Efficiency',
                         P_losses: 'Total Power Loss',
                         P_output: 'Power Output',
                         P_fw: 'Friction and Windage Losses',
                         I_path: 'Current per Armature Path'
                         }

    dict_of_units = {
                     R_f: '\\Omega',
                     V_t: 'V',
                     E_a: 'V',
                     I_a: 'A',
                     R_a: '\\Omega',
                     N: 'RPM',
                     phi: 'Wb',
                     z: '',
                     P: '',
                     a: '',
                     K_a: '',
                     T_e: 'Nm',
                     T_shaft: 'Nm',
                     omega_m: 'rad/s',
                     eff: '%',
                     P_losses: 'W',
                     P_output: 'W',
                     P_fw: 'W',
                     I_path: 'A'
                    }

    dict_of_values1 = {
                     V_t: randint(248, 252),
                     E_a: randint(231, 233),
                     I_a: randint(45, 50),
                     R_a: nm.round(uniform(0.19, 0.18), decimals=2),
                     R_f: nm.round(uniform(0.19, 0.18), decimals=2),
                     N: sample([1150], 1)[0],
                     phi: nm.round(uniform(0.01, 0.0101), decimals=4),
                     z: sample([1200], 1)[0],
                     P: 4,
                     a: 4,
                     K_a: randint(191, 193),
                     T_e: randint(94, 96),
                     T_shaft: randint(83, 84),
                     omega_m: nm.round(uniform(120, 121), decimals=2),
                     eff: nm.round(uniform(83, 84), decimals=2),
                     P_losses: randint(1800, 1850),
                     P_output: sample([10000], 1)[0],
                     P_fw: randint(600, 650),
                     I_path: 0.25*randint(40, 50)
                     }

    dict_of_values2 = {
                     V_t: randint(248, 252),
                     E_a: randint(231, 233),
                     I_a: randint(40, 50),
                     R_a: nm.round(uniform(0.19, 0.18), decimals=2),
                     R_f: nm.round(uniform(0.19, 0.18), decimals=2),
                     N: sample([1150], 1)[0],
                     phi: 0.5*nm.round(uniform(0.01, 0.0101), decimals=4),
                     z: sample([1200], 1)[0],
                     P: 4,
                     a: 2,
                     K_a: 2*randint(191, 193),
                     T_e: randint(94, 96),
                     T_shaft: randint(83, 84),
                     omega_m: nm.round(uniform(120, 121), decimals=2),
                     eff: nm.round(uniform(83, 84), decimals=2),
                     P_losses: randint(1800, 1850),
                     P_output: sample([10000], 1)[0],
                     P_fw: randint(600, 650),
                     I_path: 0.5*randint(40, 50)
                     }
    # dict_of_values2 = {
    #                  R_f: nm.round(uniform(0.18, 0.2), decimals=2),
    #                  V_t: randint(248, 252),
    #                  E_a: randint(234, 238),
    #                  I_a: randint(70, 80),
    #                  R_a: nm.round(uniform(0.18, 0.2), decimals=2),
    #                  N: sample([1125, 1150, 1200], 1)[0],
    #                  phi: 0.5*nm.round(uniform(0.01, 0.011), decimals=4),
    #                  z: sample([1125, 1150, 1200], 1)[0],
    #                  P: 4,
    #                  a: 2,
    #                  K_a: 2*randint(188, 190),
    #                  T_e: randint(150, 155),
    #                  T_shaft: randint(130, 135),
    #                  omega_m: nm.round(uniform(120, 125), decimals=2),
    #                  eff: randint(84, 86),
    #                  P_losses: randint(2900, 3100),
    #                  P_output: sample([17200, 16000, 16500], 1)[0],
    #                  P_fw: randint(600, 800),
    #                  I_path: 2*randint(18, 20),
    #                  }

    round_4dp = [phi]
    round_0dp = [z]

    # ----------
    # Functions
    # ----------


    def value(required_value, dict_of_values):
        return dict_of_values.get(required_value)


    def update_in_alist(alist, key, value):
        return [(k, v) if (k != key) else (key, value) for (k, v) in alist]


    def values_list(req_variables):
        values_to_solve = []
        for required_var in req_variables:
            z = values_for_solver.get(required_var)
            values_to_solve.append(z)
        return values_to_solve


    # ----------------
    # END - Functions
    # ----------------

    # -------------------------------
    # Independent Variable Generator
    # -------------------------------

    # independent variables are those that do not form an equation
    # this module removes a random variable from an equation
    # that had all variables existing

    independent_variables = list(list_of_variables)

    for equation in list_of_equations:

        unknowns = [x for x in equation[0] if x in independent_variables]
        # ^ gets the unknown in the equation
        # if there amount of unknowns is the same as the amount of variables
        # then remove a random equation variable from the list of independent_variables
        # in the end no variables in the list will form an equation
        # but variables can be found from it.

        # N.B. it generates a different list of independent variables each time

        if len(unknowns) == len(equation[0]):
            variables_to_remove = [a for a in unknowns if a not in always_known]
            # ^ this accounts for variables that you always want to be known. e.g. a and P
            variable_to_remove = sample(variables_to_remove, 1)[0]
            # ^ picks a random variable to be removed
            independent_variables.remove(variable_to_remove)
            # ^ removes it from the list of all variables

    # remove values that you do not want to give the user here...e.g |I_a|
    # just have a list and do some compressions

    # --------------------------------------
    # END - Independent Variable Generator
    # --------------------------------------

    # -------------------
    # Question Generator
    # -------------------

    # variables
    known = []
    known_list = []  # this is what initial variables are being randomly selected
    level_temp = []
    level_temp_vars = []
    could_be_found = []  # list of tuples (var, val) in levels
    could_be_found_list = []  # list of all tuples (var, eq) that could be found
    could_be_found_vars = []
    to_find_variables = []
    # end - variables

    while len(could_be_found) < 3:  # ensures at least 3 levels

        del known[:]
        del known_list[:]  # this is what initial variables are being randomly selected
        del level_temp[:]
        del level_temp_vars[:]
        del could_be_found[:]  # list of tuples (var, val) in levels
        del could_be_found_list[:]  # list of all tuples (var, eq) that could be found
        del could_be_found_vars[:]
        del to_find_variables[:]

        stop = False

        amt_var = randint(5, len(independent_variables))  # randomly select variables

        # known = sample(initial_variables, amt_var)  # Choose 'amt_var' elements
        # known.extend(always_known)
        # known_list = list(known)  # was 'given' previously

        # known = list(independent_variables)
        known = sample(independent_variables, amt_var)  # Choose 'amt_var' elements
        known.extend(always_known)  # adds always known
        known = list(set(known))  # remove duplicates
        known_list = list(known)

        # known = [R_a, T_e, V_f, P_fw, eff, omega_m, I_f, T_shaft, V_t]
        # known_list = list(known)

        while stop is False:

            # determine which variables can be found...len(e[0]) != 1 and
            for e in list_of_equations:  # change equation list here... put proper name in the equdict

                if len(set(e[0])-set(known)) == 1:

                    current_variable = list((set(e[0])-set(known)))[0]  # variable to be found

                    # if current_variable not in dont_solve_for:

                    try:

                        solve(e[1], current_variable)
                        # ^ try to solve for it

                        if len(solve(e[1], current_variable)) != 0:
                        # ^ ensures that there are members in solution set

                            if current_variable not in known:
                            # ^ check if the variable is already known

                                variable_equation_temp = dict(level_temp)

                                if current_variable in variable_equation_temp:

                                    # this ensures that the simplest equation is used

                                    for variable_equation_tuple in level_temp:

                                        if variable_equation_tuple[0] == current_variable:

                                            l1 = len(e[0])
                                            # ^ gets the number of variables in current equation

                                            e2 = dict_of_equations[variable_equation_tuple[1]]
                                            # ^ gets equation that find the same variable

                                            l2 = len(e2[0])
                                            # ^ gets number of variables in e2

                                            if l1 < l2:
                                                # checks if current equation uses less variables
                                                # if it does..use current equation instead
                                                update_in_alist(level_temp, current_variable, e[2])

                                else:
                                    # if variable has not been found in the level as yet
                                    level_temp.append((current_variable, e[2]))
                                    # ^ stores (var, eq) tuple is level_temp
                                    level_temp_vars.append(current_variable)
                                    # ^ stores found variables
                    except:
                        pass

            for new_variable in level_temp_vars:
                known.append(new_variable)

            if len(level_temp) == 0:  # means nothing else was
                stop = True
            elif len(could_be_found) == 3:  # give 4 levels for easy(1), moderate(1) and difficult(2)
                stop = True
                could_be_found.append(list(level_temp))  # if you need levels, otherwise use extend(temp)
                could_be_found_list.extend(list(level_temp))
                del level_temp[:]
            else:
                could_be_found.append(list(level_temp))
                # ^ use append to get list of lists...each inner list is a level
                could_be_found_list.extend(list(level_temp))
                del level_temp[:]

        could_be_found_vars.extend(level_temp_vars)

    # ===================
    # to_find generator
    # ===================

    # difficulty_level = 'easy'  # from function argument

    if difficulty_level == 'easy':
        to_find_temp = could_be_found[0]

    elif difficulty_level == 'moderate':
        to_find_temp = could_be_found[1]

    elif difficulty_level == 'difficult':
        to_find_temp = could_be_found[2:]
        to_find_temp = [item for sub_list in to_find_temp for item in sub_list]
        # ^ makes a single list of tuples

    if len(to_find_temp) <= 4:
        to_find_amt = len(to_find_temp)
    else:
        to_find_amt = choice([2, 3, 4])

    to_find_tuples = sample(to_find_temp, to_find_amt)  # choose
    to_find_tuples = [x for x in to_find_temp if x in to_find_tuples]  # reorder

    for to_find_tuple in to_find_tuples:
        to_find_variables.append(to_find_tuple[0])

    # print(could_be_found)
    # print(could_be_found_list)
    # print(could_be_found_vars)
    # print(to_find_tuples)
    # print(to_find_variables)
    # print(known_list)

    # --------------------------
    # END - Question Generator
    # --------------------------


    # -----------------
    # Value Generator
    # -----------------

    # variables
    known_tuples = []  # tuples of (initial variable, value)
    dict_of_values = sample([dict_of_values1, dict_of_values2], 1)[0]

    for variable in known_list:

        val = value(variable, dict_of_values)

        if variable in round_4dp:
            val = nm.round(val, decimals=4)
        elif variable in round_0dp:
            val = nm.round(val, decimals=0)
        else:
            val = nm.round(val, decimals=2)

        known_tuples.append((variable, val))

    # ----------------------
    # END - Value Generator
    # ----------------------


    # --------
    # Solver
    # --------

    # variables
    values_for_solver = dict(known_tuples)
    known_for_solver = list(known_list)
    could_be_found_dict = dict(could_be_found_list)
    sub_variables = []
    used_variables = []

    print("For a Series DC Motor operating at full load, you are given the following parameters: ")
    for var_val_tuple in known_tuples:  # loop through list to give the user

        # here, get var names
        variable_name = dict_of_var_names.get(var_val_tuple[0])

        # get units also
        variable_unit = dict_of_units.get(var_val_tuple[0])

        print(str(variable_name)+", "+latex(var_val_tuple[0])+" = "
              + latex(var_val_tuple[1])+" "+str(variable_unit))


    # loop through here for to find vars..show name of var
    print("\n")
    # print("Find: "+", ".join(latex(x) for x in to_find))
    print("Find the following: ")
    for to_find_variable in to_find_variables:
        variable_name = dict_of_var_names.get(to_find_variable)
        print(str(variable_name)+", "+str(to_find_variable))
    print("\n")

    # you have to have a var, val list of tuples
    solution_html = ''
    solution_html += '<ol type="a">'

    for to_find_variable in to_find_variables:  # solve for each variable in to_find_variables

        del sub_variables[:]  # clear sub_variables so it wont affect solving for other vars
        sub_variables.append(to_find_variable)  # add what you have to find

        for sub_variable in sub_variables:

            required_eq = dict_of_equations[could_be_found_dict.get(sub_variable)]
            # ^ gets the equation required to solve for the variable
            required_vars = list(required_eq[0])
            # ^ get the variables required of that equation
            required_vars.remove(sub_variable)
            # ^ removes the variable you are finding
            # so you are left with what you have to find
            # to calculate sub_variable

            unknown_variables = [x for x in required_vars if x not in known_for_solver]
            # ^ gets the variable from required_vars that hasn't been solved for already
            used_variables_temp = [y for y in required_vars if y in known_list]
            used_variables.extend(used_variables_temp)

            sub_variables.extend(unknown_variables)
            # ^ adds what needs to be found to the sub_variables list
            # so it will check to see what it depends on
            # if all is in known_for_solver nothing will be added
            # by adding what is needed to same list...you will get
            # all variables needed to solve for the initial to_find_variable

        # Now that we have a list of all variables needed
        # we need to reorder it according to the how they
        # were found in the generator
        # i.e. order sub_variables according to could_be_found_variables
        # sub_variables = [x for x in could_be_found_vars if x in sub_variables]
        solving_order = [x for x in could_be_found_vars if x in sub_variables]
        # ^ this orders the set properly for solving
        used_variables.extend(solving_order)

        solution_html += '<li>'

        for current_variable in solving_order:
            # ^ solve for each var in solving_order
            # it will be in order of what you can
            # find without having to check
            current_variable_unit = dict_of_units.get(current_variable)
            current_variable_name = dict_of_var_names.get(current_variable)

            required_eq = dict_of_equations[could_be_found_dict.get(current_variable)]
            # ^ gets the required equation
            required_vars = list(required_eq[0])
            # ^ gets the required variables
            required_vars.remove(current_variable)
            # ^ removes the variable you are trying to find
            # cause you wont need to find a value for it

            expression_to_solve = solve(required_eq[1], current_variable)
            # ^ gets the expression that will give the current variable

            # !!!! check this !!!!
            # if len(expression_to_solve) == 2:
            #     expression_to_solve = expression_to_solve[1]
            # else:
            expression_to_solve = expression_to_solve[0]
            # ^ accounts for causes where you have more than one result
            # example when finding acos (multiple values in one cycle)
            # or a square root (+ and -)

            required_values = values_list(required_vars)
            # ^ this will return a list of values
            # corresponding to the required vars

            fn = lambdify(flatten(required_vars), expression_to_solve, modules=['numpy'])

            required_value = fn(*flatten(required_values))
            # if type(required_value) is not complex:
            # required_value = float(required_value)
            # ^ solves numerically

            if current_variable in round_4dp:
                required_value = nm.round(required_value, decimals=4)
            elif current_variable in round_0dp:
                required_value = nm.round(required_value)
            else:
                required_value = nm.round(required_value, decimals=2)

            # add newly found values to lists
            known_for_solver.append(current_variable)
            values_for_solver.update({current_variable: required_value})

            solution_html += 'Using: '
            solution_html += '<ul>'

            for used_var in required_vars:
                value = values_for_solver.get(used_var)
                unit = dict_of_units.get(used_var)

                solution_html += '<li>'
                solution_html += '$'
                solution_html += str(latex(used_var))
                solution_html += '='
                solution_html += str(latex(value))
                solution_html += str(latex(unit))
                solution_html += '$'
                solution_html += '</li>'

            solution_html += '</ul>'

            print('Using:')  # to be removed, find a way to send it to web page

            for used_var in required_vars:
                value = values_for_solver.get(used_var)
                unit = dict_of_units.get(used_var)
                print(latex(used_var)+" = "+latex(value)+" "+latex(unit))
            # ^ loops gives every thing needed to find current variable

            print('Solve for '+latex(current_variable)+' with: ')

            solution_html += '<p>Solve for $'
            solution_html += str(latex(current_variable))
            solution_html += '$ using the equation: </p>'
            solution_html += '$$'
            solution_html += str(latex(required_eq[1]))
            solution_html += '$$'

            print(latex(required_eq[1]))

            if current_variable != required_eq[0][0]:
                print('-> '+latex(current_variable) +' = '+latex(expression_to_solve))
                solution_html += '$$'
                solution_html += '\Rightarrow '
                solution_html += str(latex(current_variable))
                solution_html += '='
                solution_html += str(latex(expression_to_solve))
                solution_html += '$$'
            # ^ show change of subject if current_variable was not the subject

            solution_html += 'Substituting the values give: '
            solution_html += '<p>'
            solution_html += str(current_variable_name)
            solution_html += ', '
            solution_html += '$'
            solution_html += str(latex(current_variable))
            solution_html += '='
            solution_html += str(latex(required_value))
            solution_html += str(latex(current_variable_unit))
            solution_html += '$'
            solution_html += '</p>'

            print('Substituting the values give: ')  # have to correct grammar (e.g. for 1 value)
            print(latex(current_variable)+' = '+latex(required_value)+' '
                  +latex(current_variable_unit))

            print('\n')

        solution_html += '</li>'

        print('===============================================================')
        print('\n')

    solution_html += '</ol>'



    print('END')

    used_variables = [x for x in known_tuples if x[0] in used_variables]
    # ^ extracts only the tuples that were used to give to the user
    # -------------
    # END - Solver
    # -------------

    # ----------------
    # HTML Generation
    # ----------------

    # =========
    # question
    # =========
    question_html = '<img  class="img-responsive center-block" src="/static/img/dcmotor2.svg" /><br>'

    question_html += '<p>A Series ' \
                     'DC Motor is operating under the ' \
                     'following conditions: ' \
                     '</p>'

    question_html += '<ul>'

    for var_val_tuple in used_variables:  # loop through list to give the user

        # here, get var names
        variable_name = dict_of_var_names.get(var_val_tuple[0])

        # get units also
        variable_unit = dict_of_units.get(var_val_tuple[0])

        question_html += '<li>'
        question_html += str(variable_name)
        question_html += ', $'
        question_html += str(latex(var_val_tuple[0]))
        question_html += ' = '
        question_html += str(latex(var_val_tuple[1]))
        # question_html += '$$/,$$'  # gives a space
        question_html += str(latex(variable_unit))
        question_html += '$'
        question_html += '</li>'

    question_html += '</ul>'
    question_html += '<br><p>Find: </p>'
    question_html += '<ol type="a">'

    for to_find_variable in to_find_variables:
        variable_name = dict_of_var_names.get(to_find_variable)

        question_html += '<li>'
        question_html += str(variable_name)
        question_html += ', $'
        question_html += str(latex(to_find_variable))
        question_html += '$'

    question_html += '</ol>'

    # =========
    # solution
    # =========

    # written in code due to
    # scope restrictions of
    # variables

    return(question_html, solution_html)

    # -----------------------
    # END - HTML Generation
    # -----------------------

# dcmotor2('moderate')