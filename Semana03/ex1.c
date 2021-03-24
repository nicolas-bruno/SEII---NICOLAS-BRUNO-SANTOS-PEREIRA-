#include <stdio.h>
#include <conio.h>
#include <math.h>

typedef struct {
  float real,imag;
} num_complexo;

int main() {

  num_complexo x,y,s,m;

  printf("digite a parte real e a imaginaria do primeiro completo: ");
  scanf("%f %f", &x.real, &x.imag);
  printf("digite a parte real e imaginaria do segundo complexo: ");
  scanf("%f %f", &y.real, &y.imag);

  s.real = x.real + y.real;
  s.imag = x.imag + y.imag;

    printf("a soma eh %f + (%f)i\n", s.real, s.imag);

  s.real = x.real - y.real;
  s.imag = x.imag - y.imag;

    printf("a subtracao eh %f + (%f)i\n", s.real, s.imag);

  m.real = x.real*y.real - x.imag*y.imag;
  m.imag = x.real*y.imag + x.imag*y.real;

    printf("o produto eh %f + (%f)i\n", m.real, m.imag);


    printf("a divisao eh %f + (%f)i\n", m.real, m.imag);


float m, // módulo
      f, // fase
      x, // parte real
      y; // parte imaginária

cout << “Modulo = “; cin >> m;
cout << “Fase = “; cin >> f;

f=f*M_PI/180;
x=m*cos(f);
y=m*sin(f);

cout << x << ” + j” << y;
  m.real = x.real/y.real - x.imag/y.imag;
  m.imag = x.real/y.imag + x.imag/y.real;

    printf("a forma polar eh %f + (%f)i\n", m.real, m.imag);
  

  x.imag = -x.imag;
  y.imag = -y.imag;
    
    return(0);
}