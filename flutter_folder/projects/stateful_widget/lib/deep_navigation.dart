import 'package:flutter/material.dart';

class BottomNav extends StatefulWidget {
  const BottomNav({super.key});

  @override
  State<BottomNav> createState() => _BottomNavState();
}

class _BottomNavState extends State<BottomNav> {
  int _selectedIndex = 0;

  static const List<Widget> _screenList = <Widget>[
    Center(
      child: Text('Главная страница')
    ),
    Center(
      child: Text('Поиск')
    ),
    Center(
      child: Text('Профиль')
    )
  ];

  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index;
    });
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        appBar: AppBar(
          title: Text('да'),
        ),

        body: _screenList.elementAt(_selectedIndex),
        // Захар
        bottomNavigationBar: BottomNavigationBar(
          items: [
            BottomNavigationBarItem(
              icon: Icon(Icons.home),
              label: 'Главная'
            ),
            BottomNavigationBarItem(
              icon: Icon(Icons.search),
              label: 'Поиск'
            ),
            BottomNavigationBarItem(
              icon: Icon(Icons.person),
              label: 'Профиль'
            ),
          ],
          currentIndex: _selectedIndex,
          selectedItemColor: Colors.amber,
          onTap: _onItemTapped
        ),
      ),
    );
  }
}