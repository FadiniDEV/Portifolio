import 'package:flutter/material.dart';

class AppController extends ChangeNotifier{
  static AppController instance = AppController();
  
  bool isLightTheme = true;
  changeTheme() {
    isLightTheme = !isLightTheme;
    notifyListeners();
  }
}