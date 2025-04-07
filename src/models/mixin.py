class Mixin:
    def __init__(self, *args, **kwargs):
        class_name = self.__class__.__name__
        print(f"Создан объект {class_name} с параметрами: {args}, {kwargs}")
        super().__init__(*args, **kwargs)  # Вызов __init__ родительского класса

    def __repr__(self):
        class_name = self.__class__.__name__
        # Формируем строковое представление с параметрами объекта
        return f"{class_name}({', '.join([f'{k}={v}' for k, v in self.__dict__.items()])})"
