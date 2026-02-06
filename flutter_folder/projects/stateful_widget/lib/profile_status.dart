import 'package:flutter/material.dart';
import 'package:getwidget/getwidget.dart';

class ProfileStatus extends StatefulWidget {
  const ProfileStatus({super.key});

  @override
  State<ProfileStatus> createState() => _ProfileStatusState();
}


class _ProfileStatusState extends State<ProfileStatus> {
  final List<string> _statuses = [
    'Отдыхаю',
    'Работаю',
    'В отпуске',
    'Не в сети'
  ];
}


int _currentStatusIndex = 0;

  void _cycleStatus(){
    setState(() {

      _currentStatusIndex = (_currentStatusIndex + 1) % _statuses.length;
    });

  
home:Scaffold(
  appBar: AppBar(
    title: const Text('Профиль (цикличный статус)'),
    backgroundColor: Colors.indigo,
  ),
  body: Center(
    
    child: Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        GFCard(
          title:GFListTile(
            avatar: const GFAvatar(
              child: Icon(Icons.person),
            ),
            title: const Text('Светлана'),
            style: TextStyle(fontWeight: FontWeight.bold),
          ),
          subTitle: const Text('Преподаватель математики'),
        ),
        content: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 8.0),
          child: Text(
            'Текущий статус: ${_statuses[_currentStatusIndex]}',
            style: const TextStle(fontSize: 16),
        ),
      ),
    ),

    const SizedBox(height: 20),

    GFButton(
      onPressed: _cycleStatus,
      text: "Сменить статус",
      type: GFButtonType.outline,
      blockButton: true,
    ),
    ],
  ),
),
),