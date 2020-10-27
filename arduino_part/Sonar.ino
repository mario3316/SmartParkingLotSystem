#include <NewPing.h>
#include <stdio.h>
#include <string.h>

#define SONAR_trig 2
#define SONAR_echo1 5
#define SONAR_echo2 6
#define SONAR_echo3 11
#define SONAR_echo4 8
#define SONAR_echo5 9
#define SONAR_echo6 10

#define MAX_DISTANCE 10
#define NUM_SONAR 6

int distance[NUM_SONAR];

NewPing sonar[NUM_SONAR]= 
{
  NewPing(SONAR_trig,SONAR_echo1,MAX_DISTANCE),
  NewPing(SONAR_trig,SONAR_echo2,MAX_DISTANCE),
  NewPing(SONAR_trig,SONAR_echo3,MAX_DISTANCE),
  NewPing(SONAR_trig,SONAR_echo4,MAX_DISTANCE),
  NewPing(SONAR_trig,SONAR_echo5,MAX_DISTANCE),
  NewPing(SONAR_trig,SONAR_echo6,MAX_DISTANCE)
};

void setup() {
  pinMode(SONAR_echo1, INPUT);
  pinMode(SONAR_echo2, INPUT);
  pinMode(SONAR_echo3, INPUT);
  pinMode(SONAR_echo4, INPUT);
  pinMode(SONAR_echo5, INPUT);
  pinMode(SONAR_echo6, INPUT);
  pinMode(SONAR_trig, OUTPUT);

  Serial.begin(9600);
}

void updateSonar()
{
  for(int i=0; i<NUM_SONAR; i++)
  {
    distance[i]=sonar[i].ping_cm();
  }
}

void printSonar()
{
  Serial.print("[");
  for(int i=0; i<6; i++)
  {
    Serial.print(distance[i]);
    if(i!=5)
    {
      Serial.print(",");
    }
  }
  Serial.println("]");
}

// the loop function runs over and over again forever
void loop()
{
  updateSonar();
  printSonar();
  delay(500);
}
