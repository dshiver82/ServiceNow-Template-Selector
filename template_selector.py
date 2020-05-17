#!python
import pyperclip

# Begin Program Loop
while True:

    print_menu1 = '[1] General               [5] Aspen Grade Issue'
    print_menu2 = '[2] Break / Fix           [6] SSM'
    print_menu3 = '[3] Network               [7] Aspen General'
    print_menu4 = '[4] VPN                   [8] Printer Install'

# Template Menu
    print('##################')
    print('# SNOW TEMPLATES #')
    print('##################')
    print('\n')
    print(print_menu1)
    print(print_menu2)
    print(print_menu3)
    print(print_menu4)
    print('\n')

# Follow up Menu
    print('##############################')
    print('# TICKET FOLLOW UP RESPONSES #')
    print('##############################')
    print('\n')
    print_menu6 = '[9] Provide Information to User'
    print_menu7 = '[10] Obtain Additional Information (First Attempt)'
    print_menu11 = '[11] Obtain Additional Information (Second Attempt)'
    print_menu12 = '[12] Ticket Closure Due to No Response'
    print_menu13 = '[13] Quit'
    print(print_menu6)
    print(print_menu7)
    print(print_menu11)
    print(print_menu12)
    print(print_menu13)
    print('\n')
    answer = int(input('Please enter template number: '))

### TEMPLATES ###

    # General
    if answer == 1:
        pyperclip.copy('Username: ' + '\n' + 'Contact:' + '\n' + 'Location: ' + '\n' + '\n' + 'Issue: '
                       + '\n' + '\n' + 'Troubleshooting: ')
        print('\n')
        print('Template copied to clipboard!')
        print('\n')

    # Break / Fix
    elif answer == 2:
        pyperclip.copy('Username: ' + '\n' + 'Description of Problem:' + '\n' + 'Asset Tag: ' + '\n' + 'Hostname: '
                       + '\n' + 'Make/Model: '
                       + '\n' + 'Serial Number: ' + '\n' + 'Warranty End: ' + '\n'
                       + 'Support Method: ' + '\n' + 'ODLSS Device: '
                       + '\n' + 'School Name and Address: ' + '\n' + 'Site Contact Name/Number: '
                       + '\n' + 'Access Hours: '
                       + '\n' + 'Physical Location of Device: ' + '\n' + 'Troubleshooting: '
                       + '\n' + '(Dell) Express Service Code'
                       + '\n' + 'Additional Information: ')
        print('\n')
        print('Template copied to clipboard!')
        print('\n')

    # Network Template
    elif answer == 3:
        pyperclip.copy(
            'Username: ' + '\n' + 'Contact Cell Number: ' + '\n' + 'Jack Number: '
            + '\n' + 'Copied red and yellow nodes from Solarwinds: ' + '\n' + 'Wired, Wireless or both affected?: '
            + '\n' + 'Can access internal (CPS) sites [Provide at least one example]? '
            + '\n' + 'Can access external (Internet) sites [Provide at least one example]? '
            + '\n' + 'What room(s)/hallways are experiencing the issue? ' + '\n' + 'How many users are affected? '
            + '\n' + 'Make and Type of devices (e.g Windows Laptops, Chromebooks, Macbook Airs) affected: '
            + '\n' + 'MAC addresses of at least 2 machines affected: '
            + '\n' + 'Detailed description of the problem: ' + '\n' + 'Attempted troubleshooting: ')
        print('\n')
        print('Template copied to clipboard!')
        print('\n')

    # Aspen Template
    elif answer == 7:
        pyperclip.copy('Username: ' + '\n' + 'Aspen Roles: ' + '\n' + 'Reported Issue: '
            + '\n' + 'Student IDs: ' + '\n' + 'Full Class Names: '
            + '\n' + 'Specific error message: ' + '\n' + 'Steps Taken (Tabs clicked): '
            + '\n' + 'Report Name: ' + '\n' + 'Attempted troubleshooting: ')
        print('\n')
        print('Template copied to clipboard!')
        print('\n')

    # Aspen Grade Issue Template
    elif answer == 5:
        pyperclip.copy(
            'Username: ' + '\n' + 'Students Name: ' + '\n' + 'Student IDs: '
            + '\n' + 'Homeroom: ' + '\n' + 'Related Teacher Name: '
            + '\n' + 'Class Name: ' + '\n' + 'What grade is the user reporting is inaccurate?: '
            + '\n' + 'What grade is the user reporting is accurate?: ' + '\n' + 'Detailed description of the problem: ')
        print('\n')
        print('Template copied to clipboard!')
        print('\n')

    # SSM Template
    elif answer == 6:
        pyperclip.copy(
            'Username: ' + '\n' + 'Student ID: ' + '\n' + 'Role user is calling with: '
            + '\n' + 'Which document(s) is the user receiving an error in? '
            + '\n' + 'What type of evaluation is this? (special, triennial, or annual) '
            + '\n' + 'What is the error? (Full window screenshots preferred with report name/section/error included ) '
            + '\n' + 'Which section(s) is it? '
            + '\n' + 'What are the exact steps the user takes to replicate the error/discrepancy? '
            + '\n' + 'Which report(s) does the user have concerns with? (Screenshots preferred) '
            + '\n' + 'Detailed description of the problem: ' + '\n' + 'Attempted troubleshooting: ')
        print('\n')
        print('Template copied to clipboard!')
        print('\n')

    # VPN Template
    elif answer == 4:
        pyperclip.copy('Username: ' + '\n' + 'Location: ' + '\n' + 'Device Type: '
            + '\n' + 'Operating System: ' + '\n' + 'When was the last time the user accessed the VPN?:'
            + '\n' + 'What is currently preventing them from connecting? (Specific Errors?)'
            + '\n' + 'Steps Taken (Tabs clicked): '
            + '\n' + 'Attempted Troubleshooting: '
            + '\n' + '(Any permissions issues need to be routed to Self Service)')
        print('\n')
        print('Template copied to clipboard!')
        print('\n')

    # Printer Install
    elif answer == 8:
        pyperclip.copy('Username: ' + '\n' + 'Contact: ' + '\n' + 'Location: '
                       + '\n' + 'Printer Make: ' + '\n' + 'Printer Model: '
                       + '\n' + 'Connection Method to the Printer: USB or Network (Select 1): '
                       + '\n' + 'IP Address: '
                       + '\n' + 'Computer OS:  '
                       + '\n' + 'Computer Asset Tag: ' + '\n' + 'Computer Host Name: ')
        print('\n')
        print('Template copied to clipboard!')
        print('\n')

    # Provide Information to End User
    elif answer == 9:
        pyperclip.copy('We have an important update to provide from the resolver team. Please see the update below.'
                       + '\n' + '\n' + 'Title: (This is a copy of the information in the Short Description field)'
                       + '\n' + 'Update: (This is the update we are providing)'
                       + '\n' + 'If you have any questions or concerns with the information that was provided, please contact the Service Desk.'
                       + '\n' + '\n'
                       + 'Thank you,' + '\n' + 'CPS Service Desk' + '\n' + '(773) 553-3925')
        print('\n')
        print('Template copied to clipboard!')
        print('\n')

    # Obtain Information - 1st Attempt
    elif answer == 10:
        pyperclip.copy('Additional information is needed to move forward with the resolution of your reported issue/request. Please see the additional'
                       + '\n' + 'information needed below and call the CPS Service Desk at your earliest convenience.'
                       + '\n' + '\n' + 'Title: (This is a copy of the information in the Short Description field)'
                       + '\n' + 'Additional Information Needed: (This is the information we are seeking)'
                       + '\n' + '\n'
                       + 'Thank you,' + '\n' + 'CPS Service Desk' + '\n' + '(773) 553-3925')
        print('\n')
        print('Template copied to clipboard!')
        print('\n')

    # Obtain Information - 2nd Attempt
    elif answer == 11:
        pyperclip.copy('Additional information is needed to move forward with the resolution of your reported issue/request. Please see the additional'
                      + '\n' + 'information needed below and call the CPS Service Desk at your earliest convenience.'
                      + '\n' + '\n' + 'Title: (This is a copy of the information in the Short Description field)'
                      + '\n' + 'Additional Information Needed: (This is the information we are seeking)'
                      + '\n' + '\n'
                      + 'Please note this is our final attempt to obtain this information. If we do not hear from you within 24 hours we will close this request.'
                      + 'Thank you,' + '\n' + 'CPS Service Desk' + '\n' + '(773) 553-3925')
        print('\n')
        print('Template copied to clipboard!')
        print('\n')

    # Ticket Closure due to No Response
    elif answer == 12:
        pyperclip.copy('We’ve been attempting to contact you in regards to your recent ticket with the Service Desk. Please note this request has been'
                       + '\n'
                       + 'closed due to lack of response. In the event that this is still a current issue, we will be happy to open a new request. Please call the'
                       + '\n'
                       + 'CPS Service Desk to do so.'
                       + '\n' + '\n'
                       + 'Thank you,' + '\n' + 'CPS Service Desk' + '\n' + '(773) 553-3925')

    # Quit Option
    elif answer == 13:
        break