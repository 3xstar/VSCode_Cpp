import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

  class NameApp extends StatelessWidget {
    const NameApp({super.key});

    @override
    Widget build(BuildContext context) {
      return MaterialApp(
        debugShowCheckedModeBanner: false,
        home: Scaffold(
          backgroundColor: Colors.blueGrey[50],

          body: Center(
            child: Container(
              width: 300,
              padding: const EdgeInsets.all(20),
              decoration: BoxDecoration(
                color: Colors.white,
                borderRadius: BorderRadius.circular(10),
                boxShadow: [
                  BoxShadow(color: Colors.black,
                  blurRadius: 5,
                  offset: const Offset(0, 5)
                  ),
                ]
              ),
              child: Column(
                mainAxisSize: MainAxisSize.min,
                children: [
                  Stack(
                    alignment: Alignment.center,
                    children: [
                      Container(
                        width: 350,
                        height: 150,
                        decoration: BoxDecoration(
                          borderRadius: BorderRadius.circular(15),
                          image: const DecorationImage(
                            image: AssetImage("assets/1026251959.jpg"),
                            fit: BoxFit.cover,
                          ),
                          boxShadow: [
                            BoxShadow(
                              color: Colors.grey,
                              blurRadius: 10,
                              offset: const Offset(0, 5),
                            ),
                          ],
                        ),
                      ),
                      Positioned(top: 0, left: 0,
                      child: Container(
                        width: 50,
                        height: 25,
                        decoration: BoxDecoration(
                          borderRadius: BorderRadius.circular(12),
                          color: Colors.red,
                            ),
                      child: const Center(child: Text("-45%", style: TextStyle(fontWeight: FontWeight.bold, color: Colors.white)),)
                      ),
                      ),
                    ],
                  ),
                  const SizedBox(height: 25),
                  Column(
                    children: [
                      Text('Супер классная клавиатура "NO NAME X100 ULTRA GAYMING"',
                      style: TextStyle(
                        fontWeight: FontWeight.bold,
                        fontSize: 20,
                      ),
                      textAlign: TextAlign.left,
                    ),
                    Row(mainAxisAlignment: MainAxisAlignment.start,
                    children: [
                      Icon(Icons.star, color: CupertinoColors.systemYellow,),
                      Icon(Icons.star, color: CupertinoColors.systemYellow,),
                      Icon(Icons.star, color: CupertinoColors.systemYellow,),
                      Icon(Icons.star, color: CupertinoColors.systemYellow,),
                      Icon(Icons.star, color: CupertinoColors.systemYellow,),
                      SizedBox(width: 10,),
                      Text("5",
                      style: TextStyle(
                        fontSize: 18,
                        color: Colors.grey,
                      ),
                    ),
                    ],
                    ),
                  ],
                  ),
                  const SizedBox(height: 15),
              ],
            ),
          ),
        ),
      ),
    );
  }
}