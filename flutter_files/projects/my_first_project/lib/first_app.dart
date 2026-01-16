import 'package:flutter/material.dart';

class FirstApp extends StatelessWidget {
  const FirstApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        backgroundColor: const Color.fromARGB(255, 20, 223, 223),
        appBar: AppBar(
          backgroundColor: const Color.fromARGB(255, 255, 255, 255),
          title: const Text('First flutter app'),
        ),

        body: const Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              const Text(
                'Пу пу пуууу',
                style: TextStyle(fontSize: 24),
              ),
              const Text(
                'Это текст первого приложения',
                style: TextStyle(fontSize: 24),
              ),
              const Icon(
                Icons.headphones,
                color: Color.fromARGB(255, 0, 0, 0),
                size: 50.0,
                
              ),
            ],
          )
        ) 
      )
    );
  }
}