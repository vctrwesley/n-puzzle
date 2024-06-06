# N-puzzle

Atividade para a disciplina IA (Inteligência Artificial), implementar uma solução para o N-Puzzle.

## Descrição:

A atividade consiste na implementação de uma solução para o N-Puzzle, um quebra-cabeça com N peças e um espaço disponível, organizados em um grid quadrado de dimensões sqrt(N+1)\*sqrt(N+1). O objetivo é mover as peças de forma a alcançar uma configuração específica.

## Algoritmos Implementados:

Foram implementados quatro algoritmos de busca para resolver o N-Puzzle: Busca em Largura (BFS), Busca em Profundidade Iterativa (IDS), e Busca A* com duas heurísticas diferentes (quantidade de peças erradas e distância de Manhattan). Cada algoritmo apresenta características específicas que influenciam seu desempenho e eficácia na resolução do problema. A seguir, são apresentados detalhes e comparações de desempenho entre os algoritmos:

1. Busca em Largura (BFS)
O algoritmo de Busca em Largura (BFS) explora todos os nós em cada nível antes de avançar para o próximo nível, garantindo encontrar a solução mais curta.

2. Busca em Profundidade Iterativa (IDS)
O algoritmo de Busca em Profundidade Iterativa (IDS) combina os benefícios da busca em profundidade e da busca em largura, realizando uma série de buscas em profundidade limitadas até encontrar a solução.

3. Busca A* com Heurística de Peças Erradas
A Busca A* utiliza uma heurística para priorizar a expansão de nós, neste caso, baseada na quantidade de peças fora de suas posições corretas.

4. Busca A* com Heurística de Distância de Manhattan
A heurística de distância de Manhattan leva em consideração a distância real das peças de suas posições corretas, oferecendo uma estimativa mais precisa dos custos.

Cada algoritmo foi implementado e testado para avaliar seu desempenho em termos de uso de memória, quantidade de nós expandidos, fator de ramificação médio e tempo de execução. A partir desses resultados, são feitas considerações finais sobre a eficiência e adequação de cada algoritmo para resolver o N-Puzzle.

## Contribuidores:

Se você tiver alguma dúvida ou sugestão de melhoria, sinta-se à vontade para entrar em contato com os contribuidores!

<table>
  <tr>
    <td align="center">
    <a href="https://github.com/vctrwesley">
    <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/107233909?v=4" width="100px;" alt=""/><br />
    <sub><b>Victor Wesley</b><sub>
    </a><br />
    <a href="https://www.linkedin.com/in/victor-wesley/" title="Linkedin">
    <img src="https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
    </a>
    </td>
    <td align="center">
    <a href="https://github.com/JVictor011">
    <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/91631521?s=400&u=03f358b485245072832e8fed915b5968746ae4c1&v=4" width="100px;" alt=""/><br />
    <sub><b>João Victor</b></sub>
    </a><br />
    <a href="https://www.linkedin.com/in/joao-victor-coding/" title="Linkedin">
    <img src="https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
    </a>
    </td>
</tr>
</table>