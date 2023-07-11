# API_Predictions

En este ejercicio despliego un modelo de ML en una API para su consumo. He desarrollado una API que permite consumir dicho modelo desde cualquier otra tecnología. 

He tomado como ejemplo inventado una empresa distribuidora que pretende utilizar un modelo desarrollado por el departamento de Data Science, que consigue hacer una predicción de las ventas a partir de los gastos en marketing de anuncios en televisión, radio y periódicos. Quieren incorporar estos datos dentro de su página web interna, donde comparten todo tipo de información relativa a resultados de la empresa, ventas, adquisiciones, etc... 
La web está desarrollada en AngularJS, mientras que el modelo ha sido desarrollado en Python, por lo que se precisa de una interfaz de comunicación entre ambos sistemas.

Por tanto, es necesario implementar un modelo que se pueda consumir desde la propia web, comunicándose con una BBDD para ingestar o reentrenar el modelo. 

El modelo tiene las siguientes características:

- Ofrece la predicción de ventas a partir de todos los valores de gastos en publicidad. (/v2/predict)
- Un endpoint que almacena nuevos registros en la base de datos (algo previamente creado).(/v2/ingest_data)
- La posibilidad de reentrenar de nuevo el modelo con los posibles nuevos registros que se recojan. (/v2/retrain)

NOTAS:
Si hay problemas con la ruta, ¡avisadme!.
El desarrollo de un modelo de machine learning no es realmente el objetivo del ejercicio, sino el desarrollo de una API con Flask.
