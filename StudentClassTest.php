<?php
require 'Student.php';
use PHPUnit\Framework\TestCase;
class StudentClassTest extends TestCase {
	private $name="Ihor";
	private $surname="Kandyba";
	private $group=408;
	private $StudentTestInstance;
	protected function setUp(): void
    {
        $this->StudentTestInstance = new Student();
    }
	public function testAge(){
		$this->StudentTestInstance->set_group($this->group);
		$this->assertEquals($this->group,$this->StudentTestInstance->get_group());	
	}
	public function testName(){
		$this->StudentTestInstance->set_name($this->name);
		$this->assertEquals($this->name,$this->StudentTestInstance->get_name());
	}
}