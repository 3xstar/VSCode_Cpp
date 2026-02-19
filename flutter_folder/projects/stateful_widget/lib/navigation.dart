import 'package:flutter/material.dart';

class BasicApp extends StatelessWidget{
  const BasicApp({super.key});
  
  @override
  Widget build(BuildContext context){
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Навигация наложением',
      home: FirstScreen(),
    );
  }
}

class FirstScreen extends StatefulWidget() {
  const FirstScreen({super.key});

  @override
  State<FirstScreen> createState() = _FirstScreenState();
}

class _FirstScreenState extends State<FirstScreen> {
  late TextEditingController _controller;

  @override
  void initState(){
    super.initState();
    _controller = TextEditingController();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context){
    return Scaffold(
      appBar: AppBar(
        title: Text('Первый экран'),
        backgroundColor: Colors.lightBlue,
    ),
    body: Center(
      child: Column(
        children: [
          TextField(
            controller: _controller,
            decoration: InputDecoration(
              labelText: 'Введите ваше имя'
            ),
          ),
          const.SizedBox(height: 20),

          ElevatedButton(
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(),
              );
            },
            child: Text('Передать данные'),
            ),
          ],
        )
      )
    );
  }
}

class SecondScreen extends StatelessWidget{
  const SecondScreen({super.key});

  @override
  Widget build(BuildContext context){
    return Scaffold(
      appBar: AppBar(
        title: Text('Второй экран'),
        backgroundColor: Colors.redAccent,
    ),
    body: Center(
      child: ElevatedButton(
        onPressed: () {
          Navigator.pop(context);
        }, 
        child: Text('Вернуться на первый экран')
        ),
      )
    );
  }
}