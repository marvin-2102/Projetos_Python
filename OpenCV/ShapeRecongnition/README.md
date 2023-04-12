Utilizando a aproximção por contornos, conseguimos ter uma aproximação do número de arestas de um determinado objeto, através da aproximações sucetivas de pontos na imagem, conhecido como o algoritmo de Ramer–Douglas–Peucker

Aqui, com uma imagem tratada, conseguimos com sucesso obter a identificação do objeto

![image](https://user-images.githubusercontent.com/53979368/231348347-e889f2bb-8c9c-4887-9c33-6c41fae4f0b2.png)

Já, aqui,neste exemplo, utilizando a imagem "crua", não conseguimos ter essa mesma acurácia

![image](https://user-images.githubusercontent.com/53979368/231348937-e5d40840-9ce9-4d92-925d-ca72c6f3804e.png)

Isso não significa que basta tratar as imagens e o algoritmo funcionará perfeitamente, mas é um indício do que poodemos fazer com um pouco de modelagem nos parãmetros e argumentos das funções da bilbioteca OpenCV.













Referencias:

https://en.wikipedia.org/wiki/Ramer–Douglas–Peucker_algorithm
