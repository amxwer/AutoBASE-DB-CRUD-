from datetime import datetime
from urllib import request

from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Cars, Models
from django.views import generic

# my car list
car_data = [
    ("Toyota", "Corolla", "Sedan", "150", "1.8", "Automatic", "Petrol", "2022"),
    ("Toyota", "Corolla", "Sedan", "140", "1.8", "Manual", "Petrol", "2022"),
    ("Toyota", "Camry", "Sedan", "180", "2.5", "Automatic", "Petrol", "2021"),
    ("Toyota", "Camry", "Sedan", "200", "3.0", "Automatic", "Petrol", "2021"),
    ("Honda", "Civic", "Sedan", "158", "2.0", "CVT", "Petrol", "2022"),
    ("Honda", "Civic", "Hatchback", "306", "2.0", "Manual", "Petrol", "2022"),
    ("Ford", "F-150", "Truck", "290", "3.3", "Automatic", "Petrol", "2021"),
    ("Ford", "F-150", "Truck", "400", "5.0", "Automatic", "Petrol", "2021"),
    ("Chevrolet", "Silverado", "Truck", "285", "4.3", "Automatic", "Petrol", "2022"),
    ("Chevrolet", "Silverado", "Truck", "401", "6.6", "Automatic", "Petrol", "2022"),
    ("Volkswagen", "Golf", "Hatchback", "147", "1.4", "Automatic", "Petrol", "2022"),
    ("Volkswagen", "Golf", "Hatchback", "241", "2.0", "Automatic", "Petrol", "2022"),
    ("Nissan", "Altima", "Sedan", "188", "2.5", "CVT", "Petrol", "2021"),
    ("Nissan", "Altima", "Sedan", "248", "2.0", "Variable", "Petrol", "2021"),
    ("BMW", "3 Series", "Sedan", "255", "2.0", "Automatic", "Petrol", "2021"),
    ("BMW", "3 Series", "Sedan", "473", "3.0", "Automatic", "Petrol", "2021"),
    ("Mercedes-Benz", "C-Class", "Sedan", "255", "2.0", "Automatic", "Petrol", "2021"),
    ("Mercedes-Benz", "C-Class", "Sedan", "385", "3.0", "Automatic", "Petrol", "2021"),
    ("Audi", "A3", "Sedan", "184", "2.0", "Automatic", "Petrol", "2021"),
    ("Audi", "A3", "Sedan", "228", "2.0", "Automatic", "Petrol", "2021"),
    ("Hyundai", "Elantra", "Sedan", "147", "2.0", "CVT", "Petrol", "2022"),
    ("Hyundai", "Elantra", "Sedan", "201", "2.0", "Manual", "Petrol", "2022"),
    ("Kia", "Optima", "Sedan", "185", "2.4", "6AT", "Petrol", "2021"),
    ("Kia", "Optima", "Sedan", "245", "2.0", "8AT", "Petrol", "2021"),
    ("Subaru", "Outback", "Wagon", "182", "2.5", "Automatic", "Petrol", "2022"),
    ("Subaru", "Outback", "Wagon", "260", "2.4", "Automatic", "Petrol", "2021"),
    ("Mazda", "Mazda3", "Hatchback", "186", "2.5", "Automatic", "Petrol", "2021"),
    ("Mazda", "Mazda3", "Hatchback", "227", "2.5", "Automatic", "Petrol", "2022"),
    ("Lexus", "ES", "Sedan", "203", "2.5", "8AT", "Petrol", "2022"),
    ("Lexus", "ES", "Sedan", "302", "3.5", "8AT", "Petrol", "2022"),
    ("Porsche", "911", "Coupe", "379", "3.0", "8AT", "Petrol", "2021"),
    ("Porsche", "911", "Coupe", "572", "3.7", "8AT", "Petrol", "2021"),
    ("Jeep", "Cherokee", "SUV", "180", "2.4", "9AT", "Petrol", "2021"),
    ("Jeep", "Cherokee", "SUV", "271", "3.2", "9AT", "Petrol", "2021"),
    ("Tesla", "Model 3", "Sedan", "350", "0.0", "Single-Speed", "Petrol", "2021"),
    ("Tesla", "Model 3", "Sedan", "450", "0.0", "Single-Speed", "Petrol", "2021"),
    ("Ferrari", "488", "Coupe", "661", "3.9", "7AT", "Petrol", "2021"),
    ("Ferrari", "488", "Coupe", "711", "3.9", "7AT", "Petrol", "2021"),
    ("Lamborghini", "Aventador", "Coupe", "729", "6.5", "ISR", "Petrol", "2022"),
    ("Lamborghini", "Aventador", "Coupe", "770", "6.5", "ISR", "Petrol", "2022"),
    ("Aston Martin", "Vantage", "Coupe", "503", "4.0", "Automatic", "Petrol", "2021"),
    ("Aston Martin", "Vantage", "Coupe", "542", "4.0", "Automatic", "Petrol", "2021"),
    ("Land Rover", "Range Rover", "SUV", "398", "2.0", "9AT", "Petrol", "2022"),
    ("Land Rover", "Range Rover", "SUV", "518", "4.0", "8AT", "Petrol", "2022"),
    ("Jaguar", "F-PACE", "SUV", "246", "2.0", "8AT", "Petrol", "2022"),
    ("Jaguar", "F-PACE", "SUV", "542", "5.0", "8AT", "Petrol", "2022"),
    ("Fiat", "500", "Hatchback", "69", "1.2", "Manual", "Petrol", "2022"),
    ("Fiat", "500", "Hatchback", "118", "1.4", "Manual", "Petrol", "2022"),
    ("Alfa Romeo", "Giulia", "Sedan", "276", "2.0", "8AT", "Petrol", "2021")
]


# # save our cars
# # adding our cars to db
# # Словарь для хранения объектов Cars по бренду
# cars_by_brand = {}
#
# # Итерация по car_data
# for item in car_data:
#     brand = item[0]
#     model_car = item[1]
#     key = (brand, model_car)  # Используем кортеж (бренд, модель) в качестве ключа
#
#     # Если уже есть объект Cars с этим брендом и моделью
#     if key in cars_by_brand:
#         car_instance = cars_by_brand[key]
#     else:
#         # Если нет, создаем новый объект Cars
#         car_instance = Cars(
#             brand=brand,
#             model_car=model_car,
#             type_car=item[2],  # Добавляем тип автомобиля
#             horse_power=int(item[3]),
#             engine_capacity=float(item[4]),
#             gearbox=item[5],
#             fuel_grade=item[6],
#             year_of_release=item[7]
#         )
#         cars_by_brand[key] = car_instance  # Сохраняем объект Cars в словаре
#
#     # Можно добавить другие действия с объектом Cars, если необходимо
#
#     # Сохраняем объект Cars
#     car_instance.save()
#     print(f'Car saved: {item}')
# else:
#     print(f"Invalid data format: {item}")


class MainView(generic.TemplateView):
    template_name = 'main.html'
    model = Cars

    def get(self, request, *args, **kwargs):
        return self.main_page()

    def main_page(self):
        # Получаем уникальные бренды и их количество из базы данных
        unique_brands = Cars.objects.values('brand').annotate(brand_count=Count('brand')).distinct()

        return render(self.request, self.template_name, {'unique_brands': unique_brands})


class SearchView(generic.ListView):
    model = Models
    template_name = 'brand_detail.html'

    def get(self, request, *args, **kwargs):
        return self.search_car()

    def search_car(self):
        brand = self.request.GET.get('brand', '')
        unique_brands = Cars.objects.values('brand').annotate(brand_count=Count('brand')).distinct()
        brand_names = unique_brands.values_list('brand', flat=True)
        flag = False

        if brand in brand_names:
            flag = True
            brands = Models.objects.filter(cars_id__brand__icontains=brand)
            return render(self.request, self.template_name, {'flag': flag, 'models': brands, 'brand': brand})

        else:
            unique_brands = Cars.objects.values('brand').annotate(brand_count=Count('brand')).distinct()
            return render(self.request, self.template_name, {'flag': flag, 'unique_brands': unique_brands})


# Information about each car
class DetailView(generic.DetailView):
    model = Models

    template_name = 'detail_car'

    def get(self, request, *args, **kwargs):
        return self.detail_car()

    def detail_car(request, brand, model):
        models = Cars.objects.filter(brand=brand, model_car=model).first
        return render(request, 'detail_car.html', {'models': models})

class DetailPage(generic.DetailView):
    model = Models
    template_name = 'brand_detail.html'
    context_object_name = 'car'
    slug_url_kwarg = 'brand'
    slug_field = 'brand'

    def get(self, request, *args, **kwargs):
        return self.detail_page()

    def detail_page(self):
        flag = True
        brand = self.kwargs['brand']
        models = Models.objects.filter(cars_id__brand__icontains=brand)

        return render(self.request, self.template_name, {'flag': flag, 'models': models,'brand':brand})


#
# def detail_page(request, brand: str):
#     cars = Cars.objects.filter(brand=brand)
#     print('detail')
#
#     return render(request, 'brand_detail.html', {'car': cars})
#
#
# def detail_car(request,brand, model):
#     models = Cars.objects.filter(brand=brand,model_car=model).first
#     print(models)
#
#
#     return render(request, 'detail_car.html', {'models': models})
#
#
# def search_car(request):
#     brand = request.GET.get('brand', '')
#     if brand is not None:
#         # Perform the regular brand-based search
#         cars = Cars.objects.filter(brand__icontains=brand)
#         print('good_cars:', cars)
#         print('good_brand:', brand)
#     else:
#         # Handle the case when no brand is specified
#         cars = Cars.objects.all()
#
#     return render(request, 'brand_detail.html', {'car': cars, 'brand': brand})

#
# # news bar
# def news(request):
#     return render(request, 'news.html')

# search by mark auto
