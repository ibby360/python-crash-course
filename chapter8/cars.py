def make_car(manufacture,model,**options):
    car_dict = {
        'manufacture': manufacture.title(),
        'model': model.title()
    }

    for option, value in options.items():
        car_dict[option] = value
    return car_dict

my_prado = make_car(
    'toyota', 'prado',
     color='white', 
     tow_package=True
    )
print(my_prado)

my_rav4 = make_car(
    'toyota', 
    'rav4l', 
    color='black',
    year=2019,
    doors='butterfly', 
    tow_package=True
    )
print(my_rav4)