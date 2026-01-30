import 'package:flutter/material.dart';
import 'package:helloworld/home_page.dart';
import 'package:helloworld/app_controller.dart';
import 'package:helloworld/appwidget.dart';

class LoginPage extends StatefulWidget {
  const LoginPage({super.key});

  @override
  State<LoginPage> createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {

  String user = "";
  String password = "";

  @override
  Widget build(BuildContext context) {
    final isDarkTheme = !AppController.instance.isLightTheme;
    final borderColor = isDarkTheme ? Colors.white70 : Colors.grey[700]!;

    return Scaffold(
      appBar: AppBar(
        title: Text("Login"),
        actions: [
          Icon(Icons.light_mode),
          CustomSwitch(),
        ],
      ),

      body: SingleChildScrollView(
        child: SizedBox(

          width: MediaQuery.of(context).size.width,
          height: MediaQuery.of(context).size.height,

          child: Padding(
            padding: const EdgeInsets.all(50.0),

            child: Column(

              mainAxisAlignment: MainAxisAlignment.center,
          
              children: [
                Center(
                  child: Text(
                    "Bem-vindo(a)!",
                    style: TextStyle(fontSize: 20),
                  ),
                ),
              
                SizedBox(height: 50),

                TextField(
                  onChanged: (text){
                    user = text;
                  },
                  decoration: CustomInputStyle.getFieldDecoration(
                    label: 'Usuário',
                    borderColor: borderColor,
                  ),
                ),

                SizedBox(height: 10),

                TextField(
                  onChanged: (text){
                  password = text;
                  },
                  keyboardType: TextInputType.numberWithOptions(),
                  obscureText: true,
                  decoration: CustomInputStyle.getFieldDecoration(
                    label: 'Senha',
                    borderColor: borderColor,
                  ),
                ),

                SizedBox(height: 20),

                ElevatedButton(
                  onPressed: () {
                    if(user == "Lucas" && password == "180224"){
                      Navigator.of(context).pushNamed("/home");
                    }
                    else{
                      showDialog(
                        context: context, 
                        builder: (context){
                          return AlertDialog(
                            title: Text("Erro"),
                            content: Text("Usuário ou senha incorretos."),
                            actions: [
                              TextButton(
                                onPressed: (){
                                  Navigator.pop(context);
                                }, 
                                child: Text("OK")
                              ),
                            ],
                          );
                        }
                      );
                    }
                  },
                  child: Text("Entrar"),
                ),
              ],
            )
          ),
        )
      ),
    );
  }
}