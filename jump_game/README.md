 ## Jump Game II

You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

- 0 <= j <= nums[i] and
- i + j < n

Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

### Example 1

- Input: nums = [2,3,1,1,4]
- Output: 2
- Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

### Example 2

- Input: nums = [2,3,0,1,4]
- Output: 2



### Constraints:
- 1 <= nums.length <= 104
- 0 <= nums[i] <= 1000
- It's guaranteed that you can reach nums[n - 1].


## Jogo do Pulo II

Você recebe uma matriz indexada em 0 de números inteiros de comprimento n. Você está inicialmente posicionado em nums[0].

Cada elemento nums[i] representa o comprimento máximo de um salto para frente do índice i. Em outras palavras, se você estiver em nums[i], você pode pular para qualquer nums[i + j] onde:

- 0 <= j <= nums[i] and
- i + j < n

Retorne o número mínimo de saltos para alcançar nums[n - 1]. Os casos de teste são gerados de forma que você possa alcançar nums[n - 1].

### Exemplo 1
- Entrada: nums = [2,3,1,1,4]
- Saída: 2
- Explicação: O número mínimo de saltos para alcançar o último índice é 2. Salte 1 passo do índice 0 para 1 e depois 3 passos até o último índice.

### Exemplo 2

- Entrada: nums = [2,3,0,1,4]
- Saída: 2

### Restrições:
- 1 <= nums.length <= 104
- 0 <= nums[i] <= 1000
- É garantido que você pode alcançar nums[n - 1].