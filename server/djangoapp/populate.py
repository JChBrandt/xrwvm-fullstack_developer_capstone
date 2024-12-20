from .models import CarMake, CarModel

def initiate():
    car_make_data = [
        {"name": "NISSAN", "description": "Great cars. Japanese technology"},
        {"name": "Mercedes", "description": "Great cars. German technology"},
        {"name": "Audi", "description": "Great cars. German technology"},
        {"name": "Kia", "description": "Great cars. Korean technology"},
        {"name": "Toyota", "description": "Great cars. Japanese technology"},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(
            CarMake.objects.create(name=data['name'], 
                                   description=data['description']
                                  )
        )

    # Create CarModel instances with the corresponding CarMake instances
    car_model_data = [
      {"name": "Pathfinder", "modeltype": "SUV", "year": 2023, "maker": car_make_instances[0]},
      {"name": "Qashqai", "modeltype": "SUV", "year": 2023, "maker": car_make_instances[0]},
      {"name": "XTRAIL", "modeltype": "SUV", "year": 2023, "maker": car_make_instances[0]},
      {"name": "A-Class", "modeltype": "Sedan", "year": 2023, "maker": car_make_instances[1]},
      {"name": "C-Class", "modeltype": "Sedan", "year": 2023, "maker": car_make_instances[1]},
      {"name": "E-Class", "modeltype": "Sedan", "year": 2023, "maker": car_make_instances[1]},
      {"name": "A4", "modeltype": "Sedan", "year": 2023, "maker": car_make_instances[2]},
      {"name": "A5", "modeltype": "Sedan", "year": 2023, "maker": car_make_instances[2]},
      {"name": "A6", "modeltype": "Sedan", "year": 2023, "maker": car_make_instances[2]},
      {"name": "Sorrento", "modeltype": "SUV", "year": 2023, "maker": car_make_instances[3]},
      {"name": "Carnival", "modeltype": "SUV", "year": 2023, "maker": car_make_instances[3]},
      {"name": "Cerato", "modeltype": "Sedan", "year": 2023, "maker": car_make_instances[3]},
      {"name": "Corolla", "modeltype": "Sedan", "year": 2023, "maker": car_make_instances[4]},
      {"name": "Camry", "modeltype": "Sedan", "year": 2023, "maker": car_make_instances[4]},
      {"name": "Kluger", "modeltype": "SUV", "year": 2023, "maker": car_make_instances[4]},
        # Add more CarModel instances as needed
    ]

    for data in car_model_data:
            CarModel.objects.create(
                name = data['name'], 
                maker = data['maker'], 
                modeltype = data['modeltype'], 
                year = data['year']
            )
