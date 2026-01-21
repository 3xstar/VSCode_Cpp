  import 'package:flutter/material.dart';

  class NameApp extends StatelessWidget {
    const NameApp({super.key});

    @override
    Widget build(BuildContext context) {
      return MaterialApp(
        debugShowCheckedModeBanner: false,
        home: Scaffold(
          backgroundColor: Colors.cyan[50],
          appBar: AppBar(
            backgroundColor: Colors.cyan,
            title: const Text("Визитка")
          ),
          body: Padding(
            padding: EdgeInsets.only(top:40),
            child: Container(
              margin: const EdgeInsets.all(20),
              padding: const EdgeInsets.all(20),
              decoration: BoxDecoration(
                color: Colors.white,
                borderRadius: BorderRadius.circular(10),
              ),
              child: Column(
                mainAxisSize: MainAxisSize.min,
                children: [
                  const CircleAvatar(
                    radius: 50,
                    backgroundColor: Colors.cyan,
                    child: Icon(Icons.person, size:80, color: Colors.white),
                  ),

                  SizedBox(height: 30),

                  const Text(
                    'Олег Иванов'
                    ),
                    const Text(
                      'Программист - бекэндер'
                    )

                ],

              ),
            ),
          )
        ),
      );
  }
}