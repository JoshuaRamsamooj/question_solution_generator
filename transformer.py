from random import *
from sympy import *
import numpy as nm
# import cmath as cm

# if number is complex
# convert to polar form
# have if statement for
# displaying the result
# with angle

def transformer(difficulty_level):

    # Symbols
    V_1 = Symbol('V_1')
    V_1p = Symbol('V_1^\'')
    V_2 = Symbol('V_2')
    V_2p = Symbol('V_2^\'')
    mV_2 = Symbol('|{V_2}|')
    mV_2p = Symbol('|{V^\'_2}|')
    mV_1p = Symbol('|{V^\'_1}|')
    mV_1 = Symbol('|{V_1}|')
    I_NL = Symbol('I_NL')
    I_IN = Symbol('I_IN')
    I_0 = Symbol('I_0')
    I_m = Symbol('I_m')
    I_1 = Symbol('I_1')
    I_2 = Symbol('I_2')
    N_1 = Symbol('N_1')
    N_2 = Symbol('N_2')
    mI_IN = Symbol('|{I_IN}|')
    mI_1 = Symbol('|{I_1}|')
    mI_2 = Symbol('|{I_2}|')
    R_0 = Symbol('R_0')
    X_m = Symbol('X_m')
    R_1 = Symbol('R_1')
    X_1 = Symbol('X_1')
    R_2 = Symbol('R_0')
    X_2 = Symbol('X_2')
    R_load = Symbol('R_load')
    X_load = Symbol('X_load')
    Z_load = Symbol('Z_load')
    R_eq = Symbol('R_eq')
    X_eq = Symbol('X_eq')
    Z_eq = Symbol('Z_eq')
    eff = Symbol('\\eta')
    P_losses = Symbol('P_losses')
    P_NL = Symbol('P_NL')
    P_cu = Symbol('P_cu')
    P_out = Symbol('P_out')
    P_in = Symbol('P_in')
    phi_load = Symbol('\\phi_load')
    Regulation = Symbol('R')
    j = 1j

    # Equations
    e1 = ([Regulation, mV_2, mV_2p], Eq(Regulation, ((mV_2p-mV_2)/mV_2)*100), 'e1')
    e2 = ([I_NL, I_0, I_m], Eq(I_NL, I_0 + I_m), 'e2')
    e3 = ([I_IN, I_NL, I_1], Eq(I_IN, I_NL + I_1), 'e3')
    e4 = ([V_2p, V_1p, N_1, N_2], Eq((V_2p/V_1p), (N_2/N_1)), 'e4')
    e5 = ([I_1, I_2, N_1, N_2], Eq((I_1/I_2), (N_2/N_1)), 'e5')
    e6 = ([Z_eq, R_eq, X_eq], Eq(Z_eq, R_eq + j*X_eq), 'e6')
    e7 = ([R_eq, R_1, N_1, N_2, R_2, R_load], Eq(R_eq, R_1 + ((R_2+R_load)*((N_1/N_2)**2))), 'e7')
    e8 = ([X_eq, X_1, N_1, N_2, X_2, X_load], Eq(X_eq, X_1 + ((X_2+X_load)*((N_1/N_2)**2))), 'e8')
    e9 = ([I_0, mV_1, R_0], Eq(I_0, mV_1/R_0), 'e9')
    e10 = ([V_1p, V_1, I_1, R_1, X_1], Eq(V_1p, V_1 - I_1*(R_1+j*X_1)), 'e10')
    e11 = ([V_2, V_2p, I_2, R_2, X_2], Eq(V_2, V_2p - I_2*(R_2+j*X_2)), 'e11')
    e12 = ([V_1, Z_eq, I_1], Eq(V_1, Z_eq*I_1), 'e12')
    e13 = ([I_m, mV_1, X_m], Eq(I_m, 0 + mV_1/(X_m*I)), 'e13')
    e14 = ([eff, P_out, P_in], Eq(eff, (P_out/P_in)*100), 'e14')
    e15 = ([eff, P_losses, P_in], Eq(eff, ((P_in-P_losses)/P_in)*100), 'e15')
    e16 = ([eff, P_losses, P_out], Eq(eff, (P_out/(P_out+P_losses))*100), 'e16')
    e17 = ([P_out, mV_2, mI_2, phi_load], Eq(P_out, mV_2*mI_2*cos(phi_load)), 'e17')
    e18 = ([P_in, mV_1, mI_IN, phi_load], Eq(P_in, mV_1*mI_IN*cos(phi_load)), 'e18')
    e19 = ([P_NL, I_0, R_0], Eq(P_NL, (I_0**2)*R_0), 'e19')
    e20 = ([P_cu, mI_1, R_eq], Eq(P_cu, (mI_1**2)*R_eq), 'e20')
    e21 = ([P_cu, mI_1, mI_2, R_1, R_2], Eq(P_cu, (((mI_1)**2)*R_1)+(((mI_2)**2)*R_2)), 'e21')
    e22 = ([P_losses, P_NL, P_cu], Eq(P_losses, P_cu+P_NL), 'e22')
    e23 = ([mI_1, I_1], Eq(mI_1, Abs(I_1)), 'e23')
    e24 = ([mI_2, I_2], Eq(mI_2, Abs(I_2)), 'e24')
    e25 = ([mV_1, V_1], Eq(mV_1, Abs(V_1)), 'e25')
    e26 = ([mV_2, V_2], Eq(mV_2, Abs(V_2)), 'e26')
    e27 = ([mV_1p, V_1p], Eq(mV_1p, Abs(V_1p)), 'e27')
    e28 = ([mV_2p, V_2p], Eq(mV_2p, Abs(V_2p)), 'e28')
    e29 = ([V_2, Z_load, I_2], Eq(V_2, I_2*Z_load), 'e29')
    e30 = ([Z_load, R_load, X_load], Eq(Z_load, R_load+j*X_load), 'e30')

    # e = ([], Eq(, ), 'e')

    list_of_equations = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10,
                         e11, e12, e13, e14, e15, e16, e17, e18, e19, e20,
                         e21, e22, e23, e24, e25, e26, e27, e28, e29, e30]

    dict_of_equations = {'e1': e1, 'e2': e2, 'e3': e3, 'e4': e4, 'e5': e5,
                         'e6': e6, 'e7': e7, 'e8': e8, 'e9': e9,
                         'e10': e10, 'e11': e11, 'e12': e12, 'e13': e13, 'e14': e14,
                         'e15': e15, 'e16': e16, 'e17': e17, 'e18': e18, 'e19': e19,
                         'e20': e20, 'e21': e21, 'e22': e22, 'e23': e23, 'e24': e24,
                         'e25': e25, 'e26': e26, 'e27': e27, 'e28': e28, 'e29': e29,
                         'e30': e30}

    list_of_variables = [V_1, V_1p, V_2, V_2p, mV_2, mV_2p, mV_1p, mV_1, I_NL, I_IN,
                         I_0, I_m, I_1, I_2, N_1, N_2, mI_IN, mI_1, mI_2, R_0,
                         X_m, R_1, X_1, R_2, X_2, R_eq, X_eq, Z_eq, eff, P_losses,
                         P_NL, P_cu, P_out, P_in, phi_load, Regulation, R_load, X_load, Z_load]


    #NB f was removed from the list

    dict_of_var_names = {
        V_1: 'Input Voltage',
        V_1p: 'Internal Primary Voltage',
        V_2: 'Output Voltage',
        V_2p: 'Internal Secondary Voltage',
        mV_2: 'Magnitude of Output Voltage',
        mV_1p: 'Magnitude of Internal Primary Voltage',
        mV_2p: 'Magnitude of Internal Secondary Voltage',
        mV_1: 'Magnitude of Input Voltage',
        I_NL: 'No Load Current',
        I_IN: 'Input Current',
        I_0: 'Current Representing Hysteresis and Eddy Current Losses',
        I_m: 'Magnetization Current of Transformer Core',
        I_1: 'Primary Current',
        I_2: 'Secondary Current',
        N_1: 'Number of Turns in Primary Winding',
        N_2: 'Number of Turns in Secondary Winding',
        mI_IN: 'Magnitude of Input Current',
        mI_1: 'Magnitude of Primary Current',
        mI_2: 'Magnitude of Secondary Current',
        R_0: 'Resistance Representing Hysteresis and Eddy Current Losses',
        X_m: 'Reactance of Transformer Core',
        R_1: 'Primary Resistance',
        X_1: 'Primary Reactance',
        R_load: 'Load Resistance',
        X_load: 'Load Reactance',
        Z_load: 'Load Impedance',
        R_2: 'Secondary Resistance (Including Load)',
        X_2: 'Secondary Reactance (Including Load)',
        R_eq: 'Equivalent Resistance Referred to the Primary',
        X_eq: 'Equivalent Reactance Referred to the Primary',
        Z_eq: 'Equivalent Impedance Referred to the Primary',
        eff: 'Efficiency',
        P_losses: 'Total Losses',
        P_NL: 'No Load Losses',
        P_cu: 'Copper Losses',
        P_out: 'Output Power',
        P_in: 'Input Power',
        phi_load: 'Load Power Factor Angle',
        Regulation: 'Regulation'
    }

# ADDD LOADDDDDDDDDD

    dict_of_units = {
        V_1: 'V',
        V_1p: 'V',
        V_2: 'V',
        V_2p: 'V',
        mV_2: 'V',
        mV_2p: 'V',
        mV_1p: 'V',
        mV_1: 'V',
        I_NL: 'A',
        I_IN: 'A',
        I_0: 'A',
        I_m: 'A',
        I_1: 'A',
        I_2: 'A',
        N_1: '',
        N_2: '',
        mI_IN: 'A',
        mI_1: 'A',
        mI_2: 'A',
        R_0: '\\Omega',
        X_m: '\\Omega',
        R_1: '\\Omega',
        X_1: '\\Omega',
        R_2: '\\Omega',
        X_2: '\\Omega',
        R_eq: '\\Omega',
        X_eq: '\\Omega',
        Z_eq: '\\Omega',
        R_load: '\\Omega',
        X_load: '\\Omega',
        Z_load: '\\Omega',
        eff: '\\%',
        P_losses: 'W',
        P_NL: 'W',
        P_cu: 'W',
        P_out: 'W',
        P_in: 'W',
        phi_load: 'rad',
        Regulation: '%'
    }


    dict_of_values = {
        V_1: 100,
        V_1p: 2,
        V_2: 364-8j,
        V_2p: 376-6j,
        mV_2: 364.09,
        mV_2p: 6,
        mV_1p: 7,
        mV_1: 100,
        I_NL: 0.5-2j,
        I_IN: 1.5-4j,
        I_0: 11,
        I_m: 12,
        I_1: 1-2j,
        I_2: 0.25-0.5j,
        N_1: 50,
        N_2: 200,
        mI_IN: 17,
        mI_1: 18,
        mI_2: 19,
        R_0: 20,
        X_m: 21,
        R_1: 0.5,
        X_1: 2.5,
        R_2: 8,
        X_2: 24,
        R_eq: 26,
        X_eq: 27,
        Z_eq: 28,
        R_load: 304,
        X_load: 576,
        Z_load: 304+376j,
        eff: 90,
        P_losses: 30,
        P_NL: 50,
        P_cu: 1.12,
        P_out: 33,
        P_in: 34,
        phi_load: 35,
        Regulation: 36
    }

    round_3dp = []
    round_0dp = []
    always_known = []
    complex_rect = [I_NL, Z_eq, Z_load]

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

    d2r = lambda x: nm.deg2rad(x)
    r2d = lambda x: nm.rad2deg(x)

    to_rd = lambda m, d: m*nm.exp(1j*d2r(d))
    to_pd = lambda x: (nm.abs(x), r2d(nm.angle(x)))


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
        # ^ gets the unknown in the
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


    print(independent_variables)
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

    # difficulty_level = 'moderate'  # from function argument

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
    # dict_of_values = sample([dict_of_values1, dict_of_values2], 1)[0]

    for variable in known_list:

        val = value(variable, dict_of_values)

        if variable in round_3dp:
            val = nm.round(val, decimals=3)
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
            # print(required_eq)
            # print(sub_variable)
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
            if len(expression_to_solve) == 2:
                expression_to_solve = expression_to_solve[1]
            else:
                expression_to_solve = expression_to_solve[0]
            # ^ accounts for causes where you have more than one result
            # example when finding acos (multiple values in one cycle)
            # or a square root (+ and -)

            # if current_variable == theta:
            #     expression_to_solve = expression_to_solve[1]
            #     # ^ because of way sympy solves
            # else:
            #     expression_to_solve = expression_to_solve[0]


            required_values = values_list(required_vars)
            # ^ this will return a list of values
            # corresponding to the required vars

            # print(required_eq)
            # print(current_variable)
            # print(required_values)
            # print(required_vars)

            fn = lambdify(flatten(required_vars), expression_to_solve, modules=['numpy'])

            required_value = fn(*flatten(required_values))
            # if type(required_value) is not complex:
            # required_value = float(required_value)
            # ^ solves numerically
            # print(required_value)

            if current_variable in round_3dp:
                required_value = nm.round(required_value, decimals=3)
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

                if type(value) is nm.complex128:
                    value = nm.round(to_pd(value), decimals=2)
                    solution_html += '<li>'
                    solution_html += '$'
                    solution_html += str(latex(used_var))
                    solution_html += '='
                    solution_html += str(latex(value[0]))
                    solution_html += '\\angle'
                    solution_html += str(latex(value[1]))
                    solution_html += str(latex(unit))
                    solution_html += '$'
                    solution_html += '</li>'

                else:
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
            print(type(required_value))
            if type(required_value) is nm.complex128:
                print('check')
                required_value = nm.round(to_pd(required_value), decimals=2)
                solution_html += str(latex(required_value[0]))
                solution_html += '\\angle'
                solution_html += str(latex(required_value[1]))
            else:
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
    question_html = ''

    question_html += '<p>' \
                     'An Induction Motor is operating under the ' \
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

# transformer('difficult')