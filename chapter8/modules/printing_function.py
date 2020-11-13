def print_models(unprinted_designs,completed_models):
    """ 
    printing each design untill there is none left
    moving each design to completed_model after printing
    """

    while unprinted_designs:
        current_design = unprinted_designs.pop()

    # creating a 3d print fom the design
    print(f"printing model: {current_design}.")
    completed_models.append(current_design)

def show_completed_models(completed_models):
    """ 
    show all models that were printed
    """
    print("\nThe following model have been printed.")
    for completed_model in completed_models:
        print(completed_model)