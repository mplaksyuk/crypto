run program:

```console
python{your python version} filename.py
```

or

```console
python filename.py
```

Algorithm RSA
RSA (Rivest-Shamir-Adleman) є криптографічним алгоритмом, який використовується для шифрування та підписування даних. Його назва походить від прізвищ розробників - Рональда Райвеста, Аді Шаміра та Леонарда Адлемана. Алгоритм RSA базується на математичних властивостях чисел інодісів.
Основними складовими алгоритму RSA є наступні кроки:
Генерація ключів:

* Крок 1: Вибір двох великих простих чисел, які називаються p та q.
* Крок 2: Обчислення модуля N шляхом перемноження p та q: N = p * q.
* Крок 3: Обчислення функції Ойлера (Euler's totient function) φ(N), де φ(N) = (p-1) * (q-1).
* Крок 4: Вибір цілого числа e (1 < e < φ(N)), такого що НСД (Найбільший Спільний Дільник) (e, φ(N)) = 1. Число e стає публічним ключем для шифрування.
* Крок 5: Обчислення числа d, яке задовольняє рівність (e * d) mod φ(N) = 1. Число d стає приватним ключем для дешифрування.

Шифрування:
При використанні алгоритму RSA, відкритий текст або повідомлення представляється у вигляді числа m, де 0 <= m < N. Шифрування виконується з використанням публічного ключа (e) за допомогою формули c = (m^e) mod N, де c - шифротекст, що отримується.

Дешифрування:
Шифротекст c може бути розшифрований за допомогою приватного ключа (d) за допомогою формули m = (c^d) mod N. Результатом буде вихідний текст, який був зашифрований.

Diffie-Hellman protocol
Протокол Діффі-Геллмана (Diffie-Hellman protocol) - це криптографічний протокол, який дозволяє двом сторонам, що знаходяться у відкритому комунікаційному каналі, встановити спільний секретний ключ безпосередньо між собою, навіть якщо комунікаційний канал є ненадійним і підатливим до прослуховування.
Основні кроки протоколу Діффі-Геллмана такі:
Параметри системи:

* Крок 1: Обрання простого числа p із великими значеннями і числа g, яке є примітивним коренем за модулем p. Ці параметри відомі всім сторонам протоколу.

Генерація ключів:

* Крок 2: Кожна сторона обирає секретне число, яке називається приватним ключем. Нехай a - приватний ключ першої сторони, а b - приватний ключ другої сторони. Обидві сторони зберігають свої приватні ключі в секреті.
* Крок 3: Кожна сторона обчислює відкритий ключ, використовуючи спільні параметри p і g, а також свій приватний ключ:
* Перша сторона обчислює A = (g^a) mod p і відправляє A другій стороні.
* Друга сторона обчислює B = (g^b) mod p і відправляє B першій стороні.
  Встановлення спільного секретного ключа:
* Крок 4: Перша сторона обчислює спільний секретний ключ за формулою s = (B^a) mod p.
* Крок 5: Друга сторона також обчислює спільний секретний ключ за формулою s = (A^b) mod p.

Після цих кроків обидві сторони мають однаковий спільний секретний ключ s, який може бути використаний для подальшого шифрування і розшифрування повідомлень.

Протокол Діффі-Геллмана базується на складності обчислення дискретного логарифму, тобто знаходження значення x в рівнянні g^x ≡ A (mod p). Ця складність робить його важким для зламування з боку потенційного зловмисника, який спостерігає комунікацію.
