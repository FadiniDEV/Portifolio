import 'package:flutter/material.dart';
import 'package:helloworld/app_controller.dart';

class HomePage extends StatefulWidget {
  @override
  State<HomePage> createState() {
    return HomePageState();
  }
}

class HomePageState extends State<HomePage> {
  int counter = 0;
  
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Contador Simples"),
      ),
      
      body: Center(
          child: Switch(
          value: AppController.instance.isLightTheme, 
          onChanged: (value){
            AppController.instance.changeTheme();
            }),
      ),

      floatingActionButton: FloatingActionButton(
        child: Icon(Icons.add),
        onPressed: () { 
          setState(() {
          counter++;
          });
        },
      ),
      
    );
  }
}