import 'package:flutter/material.dart';

class CardApp extends StatelessWidget {
  const CardApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        body: Column(
          children: [
            Container(
              margin: EdgeInsets.all(20),
              padding: EdgeInsets.all(15),
              decoration: BoxDecoration(
                gradient: LinearGradient(colors: [Colors.yellow, Colors.cyanAccent],),
                borderRadius: BorderRadius.circular(10),
                boxShadow: [
                  BoxShadow(
                      color: Colors.grey,
                      blurRadius: 10,
                    ),
                  ],
                ),
          child: Row(
            children: [
              Container(
                decoration: BoxDecoration(
                  color: Colors.white,
                  borderRadius: BorderRadius.circular(8),
                  boxShadow: [
                    BoxShadow(
                      color: Colors.black.withOpacity(0.3),
                      blurRadius: 15,
                      spreadRadius: 2,
                      offset: Offset(5, 5),
                    ),
                ],
              ),
              padding: EdgeInsets.all(8),
              child:Text('#2007'),
            ),
            SizedBox(width: 20),
            Expanded(
              child: Text(textAlign: TextAlign.center,
              style: TextStyle(fontWeight: FontWeight.bold,),
              "Доставка пришла! Заберите сегодня")
              ),
            Container(
                padding: EdgeInsets.all(8),
                decoration: BoxDecoration(
                  color: Colors.white,
                  borderRadius: BorderRadius.circular(10),
                  boxShadow: [
                    BoxShadow(
                      color: Colors.black.withOpacity(0.3),
                      blurRadius: 15,
                      offset: Offset(5, 5),
                    ),
                  ]
                ),
                child: Icon(Icons.location_on),
              )
            ],
          ),
        ),
      ],  
    ),
  ),
); 
}
}