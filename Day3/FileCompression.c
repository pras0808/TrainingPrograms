#include <stdio.h>
#include <stdlib.h>
void compress_file(const char *input_filename, const char *output_filename) {
    FILE *in = fopen(input_filename, "r");
    FILE *out = fopen(output_filename, "w");
    if (in == NULL || out == NULL) {
        printf("Error opening files!\n");
        return;
    }
    int current_char = fgetc(in);
    if (current_char == EOF) {
        fclose(in);
        fclose(out);
        return;
    }
    int count = 1;
    int next_char;
    while ((next_char = fgetc(in)) != EOF) {
        if (next_char == current_char) {
            count++; 
        } else {
            fprintf(out, "%c%d", current_char, count);
            current_char = next_char;
            count = 1; 
        }
    }
    fprintf(out, "%c%d", current_char, count);
    fclose(in);
    fclose(out);
    printf("File compressed successfully!\n");
}
void decompress_file(const char *input_filename, const char *output_filename) {
    FILE *in = fopen(input_filename, "r");
    FILE *out = fopen(output_filename, "w");
    if (in == NULL || out == NULL) {
        printf("Error opening files!\n");
        return;
    }
    int ch;
    int count;
    while ((ch = fgetc(in)) != EOF) {
        if (fscanf(in, "%d", &count) == 1) {
            for (int i = 0; i < count; i++) {
                fputc(ch, out);
            }
        }
    }
    fclose(in);
    fclose(out);
    printf("File decompressed successfully!\n");
}
int main() {
    int choice;
    printf("--- File Zipper (RLE) ---\n");
    printf("1. Compress File\n");
    printf("2. Decompress File\n");
    printf("Enter choice (1 or 2): ");
    scanf("%d", &choice);
    if (choice == 1) {
        compress_file("input.txt", "compressed.txt");
    } else if (choice == 2) {
        decompress_file("compressed.txt", "output.txt");
    } else {
        printf("Invalid choice!\n");
    }
    return 0;
}
