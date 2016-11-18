#include <16f877.h>         // This is the header for the PIC i'm using
#device ADC=10              // Sets the ADC to be 10 bit wide
#use delay (clock=20000000) // sets the clock for 20MHz
#include <cuscostdio.h>     // This is the standard library for the board

main(){
  output_a(0x00);
  output_b(0x00);
  output_c(0x00);
  output_d(0x00);
  int timing = 1;

  while(1){
    delay_us(5);
    output_high(BUZZER);
    delay_us(timing);
    output_low(BUZZER);
    if (timing <= 1000) timing++;
    else timing--;
  }
}
