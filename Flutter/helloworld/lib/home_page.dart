import 'package:flutter/material.dart';

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
        backgroundColor: Color(Colors.red.value),
      ),
      
      body: Center(
          child: GestureDetector(
            child: Text(
              "Você clicou $counter vezes",
              style: TextStyle(fontSize: 20),
            ), 
              onTap: () {
                setState(() {
                  counter++;
                });
              },
          )
      ),

      floatingActionButton: FloatingActionButton(
        child: Icon(Icons.add),
        backgroundColor: Color(Colors.red.value),
        onPressed: () { 
          setState(() {
          counter++;
          });
        },
      ),
      
    );
  }
}