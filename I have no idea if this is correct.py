import colorama

introspection_results = dir(colorama)
print(introspection_results)

#клас Fore
Fore.RED      # Червоний
Fore.GREEN    # Зелений
Fore.YELLOW   # Жовтий
Fore.BLUE     # Синій
Fore.RESET    # Скинути тільки колір тексту

#клас Back
Back.RED      #Червоний фон
Back.WHITE    #Білий фон
Back.RESET    #Скинути тільки фон

#клас Style
Style.BRIGHT     #Яскравий/Жирний текст
Style.DIM        #Тьмяний текст
Style.NORMAL     #Звичайний текст
Style.RESET_ALL  #Повне скидання
