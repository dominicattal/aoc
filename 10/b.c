#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <omp.h>

typedef struct {
    int num_joltages;
    int num_buttons;
    int buttons[32];
    int joltages[32];
} Problem;

int solve(Problem* problem)
{
}

int main()
{
    FILE* fptr;
    Problem* problems;
    char line[512];
    int problem_id;
    char* tok;
    char* prev_tok;
}
