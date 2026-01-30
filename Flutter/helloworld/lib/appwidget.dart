import 'package:flutter/material.dart';
import 'package:helloworld/app_controller.dart';
import 'package:helloworld/home_page.dart';
import 'package:helloworld/login_page.dart';

class AppWidget extends StatelessWidget{
  @override
  Widget build(BuildContext context) {
    return AnimatedBuilder(
      animation: AppController.instance,
      builder: (context, child) {
        final brightness = AppController.instance.isLightTheme 
          ? Brightness.light
          : Brightness.dark;
        return MaterialApp(
          theme: ThemeData(
            colorScheme: ColorScheme.fromSwatch(
              primarySwatch: Colors.red,
              brightness: brightness,
            ),
            brightness: brightness,
          ),
          home: LoginPage(),
        );
      },
    );
  }
}