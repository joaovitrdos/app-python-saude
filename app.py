from menus import welcome, show_menu, get_info
def run_app() :
    welcome()
    patient_info = get_info ()
    show_menu(patient_info)