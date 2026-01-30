import 'package:flutter/material.dart';
import 'package:helloworld/app_controller.dart';
import 'package:helloworld/home_page.dart';
import 'package:helloworld/login_page.dart';

class CustomInputStyle {
  static InputDecoration getFieldDecoration({
    required String label,
    required Color borderColor,
  }) {
    return InputDecoration(
      enabledBorder: OutlineInputBorder(
        borderSide: BorderSide(color: borderColor, width: 1.5),
      ),
      focusedBorder: OutlineInputBorder(
        borderSide: BorderSide(color: Colors.red, width: 2),
      ),
      labelText: label,
    );
  }
}

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
          routes: {
            "/": (context) => LoginPage(),
            "/home": (context) => HomePage(),
          },
        );
      },
    );
  }
}