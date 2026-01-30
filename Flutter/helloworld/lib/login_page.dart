import 'package:flutter/material.dart';
import 'package:helloworld/home_page.dart';

class LoginPage extends StatefulWidget {
  const LoginPage({super.key});

  @override
  State<LoginPage> createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Login"),
        actions: [
          Icon(Icons.light_mode),
          CustomSwitch(),
        ],
      ),

      body: SizedBox(
        
        width: double.infinity,
        height: double.infinity,
        child: Padding(
          padding: const EdgeInsets.all(50.0),

          child: Column(

            mainAxisAlignment: MainAxisAlignment.center,
          
            children: [
              TextField(
                decoration: InputDecoration(
                  border: OutlineInputBorder(),
                  labelText: 'Username',
                ),
              ),

              TextField(
                keyboardType: TextInputType.numberWithOptions(),
                obscureText: true,
                decoration: InputDecoration(
                  border: OutlineInputBorder(),
                  labelText: 'Password',
                ),
              ),
            ],
          )
        ),
      ),
    );
  }
}