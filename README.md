# KU Smart Parking Lot System

## ������Ʈ �Ұ�

### 1. ������Ʈ ��ǥ �� ���

#### ��. ���� ��ǥ

? ������Ʈ�� : �Ƶ��̳븦 �̿��� ����Ʈ ������ �ڸ� �ȳ� �ý���

     - ������Ʈ ���� : �� ���� ��������� �����Ͽ� �����ϰ� �������� �̿��ϴ� �������� ���Ǽ��� ���� �� �ڸ��� �ȳ�, ���� ���ִ� �ý���

     - ������Ʈ ���� ���� : ��ȭ��, ������, ��ȭ���� ���������� �� ������� ���� ������ ���� �����忡�� ���� ������ ã�� ���� ���� ���� �Ű� �ٴϸ� ���� ���� ���� ������ �߽��ϴ�. �̷� ��ҿ����� ������ �ϱ� ���� ���� �ð��� �ɸ��� ���� �����ڵ��� ������ ���ο��� �ڸ��� ã�� ���� â���� �θ����Ÿ��� �����ϱ� ������ ���˻���� ����� �ֽ��ϴ�. �׷��� ��Ʈ��ũ ����� ���� �Ƶ��̳�� ����Ʈ ������ �ڸ� �ȳ� �ý����� ��Ʈ��ũ ���α׷��� ������Ʈ ������ �����ϰ� �Ǿ����ϴ�.

? �ֿ� ���� ���

    - ������ ���ڸ� ���� ����, ������ ó��
        ? �Ƶ��̳뿡 ������ �Ÿ� ������ Ȱ���Ͽ� �� ������ ��ġ�� ���� ���� �ִ��� ������ ������ �����Ͽ� �����͸� ó���ϰ�, �� ������ �� ���� �Ǿ� �ִ� ���� ��, ���� ���� ������ �ڸ��� �Ǻ��մϴ�.

    - ������ �ȳ��� ���� GUI
        ? �� �������� GUI�� ���� �������� �� �ڸ��� ã�� �̸� �����Ͽ� �ٷ� ������ �� �ֵ��� ������ �ݴϴ�.

#### ��. ������Ʈ ���

? �Ƶ��̳븦 �̿��� ����Ʈ ������ �ý���

- ������Ʈ ���� : �� �������� �� ������ ��ġ�� �Ƶ��̳� ���带 ���� �������� ������ ������ ����ְ�, ������ ����(Local Server)���� �������� ����Ͽ� �������� ������ �Ǻ�, ���� ������ �����Ͽ� ���� ���������� ��� �������� �������� ���� �����ϰ�, Client���� ���Ӱ� Admin�� ������ �����մϴ�.

### 2. ������Ʈ ���� ȯ��

? �ϵ���� : �Ƶ��̳� Uno ����, ������ ���� 5��
? OS : Windows 10 Professional x64
? Python 3.8.0 , c++ - GUI Library : PyQt5
? IDE : Pycharm community edition 19.01.03, Arduino IDE

### 3. �ٽ� �˰�����

? �Ƶ��̳� - ���� ���� ������ �����κ��� �������� �޾ƿ�
? Arduino���� ���̺귯�� �� NewPing ���̺귯�� ��� - 0.5�� ������ ������ ������ �迭�� Update ���� - Serial print�� ����Ͽ� Local Server�� Client�� ����

? Local Server�� Client - Local Server�� Client�� �Ƶ��̳�κ��� Python serial ���̺귯���� �������� �޾ƿ�. - ���ڿ� ���·� �޾ƿ� ���� ������ strip ���ְ� list�� ������� - �ش� list�� 0.5�� ������ Local Server�� ����

? Local Server - ���� ������ ���� �� �ڽ��� ID�� ���� (ex. �Ű��а�) - �� �����忡�� ���� ���� ���� �� �ְ�, �� �����帶���� ������ �����ϹǷ� client ������ thread�� ó���Ͽ� ���� ���ӱ��� - �� client�鿡�� ���� �������� 5 ���� ������ ���� �Ұ���, 5 �̻��̸� ���� ������ �Ǻ��Ͽ� { location, Floor, 0, 1, 2, 3, 4 } ������ dictionary�� ���� - �ش� dictionary�� 0.5�� ������ ���� ������ ����

? Main Server

    - ������ �ڵ鷯, Ŭ���̾�Ʈ �ڵ鷯, ������ �ڵ鷯 3���� thread�� �� ��Ʈ�� ���� ����ó�� - ������ �ڵ鷯������ ������(Local Server)���� ������ ó���ϰ� ������ dictionary�� ���������� update�Ͽ� ������ ����

    - Ŭ���̾�Ʈ �ڵ鷯������ Ŭ���̾�Ʈ�� ���� ������ ó���ϰ� Ŭ���̾�Ʈ�κ��� � ������������ string �� ��ȸ���� ���������� string�� �޾� �ش� ��û�� ����

    - ������ �ڵ鷯������ ������ ���ӽ� �ǽð� ������ �������� ����ؼ� Admin���� �����ְ� ���� ������ Client���� ID�� ����.

    - ���� ������ ������ txt���·� �� ������ ���� �����Ͽ� �ǽð����� write ����

? Client - ���μ����� ���ӽ� �ڽ��� ID�� ���Ƿ� ���� - ui �� pushButton event�� ó���Ͽ� ��� �������� ��ȸ, ���� ���� string�� ���� ������ ���� - ���� �������� �޾ƿ� dictionary�� ui�� ���

? Admin - ui�� testBrowser�� �н����带 �Է¹޾� �ش� string�� ���� ������ �����Ͽ� ���μ����� string�� �н����带 ���� �� ��� ���� Admin���� ���� - ���� �� ���� �����κ��� ��� Receive�� �Ͽ� ui �� ���

### 4. System Design

<img src="https://user-images.githubusercontent.com/51048267/97243487-c909d780-1839-11eb-9fd5-53d62799ad71.png" width="100%"></img>

### 5. ������Ʈ ���࿡ ���� ������ �� ���� ���

#### ��. ������

? ��� ���������� Multi ? Thread�� ����Ͽ� ���� �϶� - parkinglot, admin, client �� ���� thread ��� - �� �����忡�� �ǽð� ������ �޾ƿ��� admin �� client���� request�� ó�� - Client �� 50�� ���ӽ� ���ϰ� �߻�

? ��������� �ڷᱸ���� �̸� ���س��Ƽ� Ȯ�强�� ������ - singong, sanhak, haebong, gongdae 4���� �ڷᱸ���� �̸� ���س��� - ���ο� ������ ���Խ� (ex. ��õ���) ���ο� �ڷᱸ���� �����������

#### ��. �������

? Multi-Process �� Multi-thread�� ������ ��� - ū �� ���� �ڵ鷯 (parkinglot, admin, client)�� ��Ƽ ���μ����� �����ϰ� �ش� ���μ��� �������� ��Ƽ ������� ó���ϸ� ���ϸ� ���ϼ� ����

? �ڷᱸ���� ���� list ���� - ���ο� �������� ���Եɶ����� list�� �ش� ������ ID ������ �ڷᱸ���� append ���� - �� �������� ������ ���� list�� index�� �����Ͽ� ������ �޾ƿ� �� ����