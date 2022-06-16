from setuptools import setup, find_packages 
setup(
	# 배포할 패키지의 이름
    name = 'pipdisttest',
    # 배포할 패키지의 버전
	version = '0.1', 
    # 배포할 패키지에 대한 설명
	description = 'pypi deploy test', 
	# 배포하는 사람의 이름
    author = 'stone2f', 
	# 배포하는 사람의 메일주소
    author_email = 'stone2f@gmail.com', 
	# 배포하는 패키지의 url(보통 github 링크)
    url = 'https://github.com/seokhwaLee/pipdisttest.git', 
    # 배포하는 패키지의 다운로드 url
	download_url = 'https://github.com/seokhwaLee/pipdisttest/archive/refs/heads/main.zip', 
	# 해당 패키지를 사용하기 위해 필요한 패키지 (현재 패키지를 install할때 함께 install 됨)
	install_requires = ['numpy'],
	# 등록하고자 하는 패키지(제외하고자 하는 파일 exclude에 기재)  
	packages = find_packages(exclude = []),
	# 패키지의 키워드를 적습니다.    
	keywords = ['pypi deploy'], 
	# 해당 패키지를 사용하기 위해 필요한 파이썬 버전을 기재  
	python_requires = '>=3', 
	# 파이썬 파일이 아닌 다른 파일을 포함시키고 싶다면 package_data에 포함
    package_data = {},
	# 위의 package_data에 대한 설정을 하였다면 zip_safe설정
	zip_safe = False, 
	# PyPI에 등록될 메타 데이터 설정(실제 빌드에 영향X)
	classifiers = [
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.2',
		'Programming Language :: Python :: 3.3', 
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
	],
)