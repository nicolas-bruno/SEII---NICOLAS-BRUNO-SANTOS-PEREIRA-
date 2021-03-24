#include <stdio.h>
#include <stdlib.h>

int main(int argc,char **argv)
{
   char ch;
   FILE *source, *target, *aloc;
   int max = 1000;

   printf("Abrindo carregando arquivo...\n");


   source = fopen(argv[1], "r");

   aloc = (char *) malloc(max * sizeof(char));


   if (source == NULL)
   {
      printf("falha, aperte qualquer tecla para fechar...\n");
      exit(EXIT_FAILURE);
   }

   target = fopen(argv[2], "w");



   if (target == NULL)
   {
      fclose(source);
      printf("falha, aperte qualquer tecla para fechar...\n");
      exit(EXIT_FAILURE);
   }

   while ((ch = fgetc(source)) != EOF)
      fputc(ch, target);

   printf("Copiado com sucesso!\n");

   fclose(source);
   fclose(target);

   return 0;
}