A, B, C, D = list(map(float, input().split()))
avg = (A * 2 + B * 3 + C * 4 + D * 1) / 10
print(f"Media: {avg:.1f}")

if avg >= 7.0:
    print("Aluno aprovado.")
elif avg < 5:
    print("Aluno reprovado.")
elif avg >= 5.0 and avg <= 6.9:
    print("Aluno em exame.")
    E = float(input())
    print(f"Nota do exame: {E:.1f}")
    avg2 = (E + avg) / 2
    if avg2 >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {avg2:.1f}")
   