# PythonTutorial
# Git conflict
    -) resolve conflict
        1) accept the current change or the incoming change
        2) git add <file name>
        3) git commit -m '<message, ex: resolve conflict>'
    -) commit
        *) git add <file name> (do it only one time, for the first time)
        1) git commit -m '<message, ex: finished exercise 1, finished the Reading DICOM function>'
        2) git push (can commit serveral times, then git push)

# Coding Convention
    +) Writing code for machine understanding is not enough
    +) Writing code for human understanding (for your friends, supervisors)
    +) Give meaningful name for files, variables, functions
    +) Provide docs (doc string)
        *) Because after 3 weeks, you will forget everything
                only God can understand what you have done
    +) Variable name: always start with a noun
        *) counter = 0, checker = 0
    +) Function name: always start with a verb (function are designed to do an action)
        *) is_prime_number()
        *) read_dicom_file()
    +) expression
        *) a + b (not a+b)
    +) Indentation
        *) Refer soft-indentation
            ex: hard indentation: \t\t\t\t (tab key)
                soft-indentation: \s\s\s\s (space key)
            *) because tab key is defined by operation system (OS)
                ==> different OS will provide different definition for tab key
                ==> but, space is always the same in all OS
        *) always use 4 spaces