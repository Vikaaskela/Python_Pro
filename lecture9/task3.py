#Task 3
#Створіть клас "Прямокутник", який має приватні властивості width і height. Використайте декоратори 
#@property для створення властивостей width і height, які повертають значення цих властивостей. Визначте 
#метод __setattr__, який забороняє безпосередню зміну значень width і height. Використовуйте метод __getattr__, 
#який повертає повідомлення про те, що властивість не існує, якщо спробувати отримати доступ до неіснуючої властивості.
#Додайте метод area, який обчислює площу прямокутника. Створіть об'єкт прямокутника і спробуйте змінити значення width і height, 
#а також отримати доступ до неіснуючої властивості та обчислити площу прямокутника.