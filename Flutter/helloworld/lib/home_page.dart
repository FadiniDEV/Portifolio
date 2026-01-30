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
        actions: [
          Icon(Icons.light_mode),
          CustomSwitch(),
        ],
      ),
      
      body: Container(

        width: double.infinity,
        height: double.infinity,

        child: Column(

          mainAxisAlignment: MainAxisAlignment.center,

          children: [
            Text(
              "Você clicou $counter vezes",
              style: TextStyle(fontSize: 25),
            ),

            Text(
              "Por favor, clique mais!",
              style: TextStyle(fontSize: 16),
            ),
          ],
        ),
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

class CustomSwitch extends StatelessWidget {
  const CustomSwitch({super.key});

  @override
  Widget build(BuildContext context) {
    return Switch(
          value: AppController.instance.isLightTheme, 
          onChanged: (value){
            AppController.instance.changeTheme();
            });
  }
}