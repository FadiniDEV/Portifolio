#include <stdio.h>

int main() {
    float nota1, nota2, media;
    
    printf("Digite a Primeira Nota: ");
    scanf("%f", &nota1);

    printf("Digite a Segunda Nota: ");
    scanf("%f", &nota2);

    media = (nota1 + nota2) / 2;
    printf("\n\nSua média é: %.2f\n", media);
    
    if (media >= 7) {
        printf("Aprovado\n\n\n");
    } else {
        printf("Reprovado\n\n\n");
    }

    return 0;
}