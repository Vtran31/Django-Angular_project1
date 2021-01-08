import { Component, OnInit } from '@angular/core';
import { SharedService } from 'src/app/shared.service';

@Component({
  selector: 'app-show-emp',
  templateUrl: './show-emp.component.html',
  styleUrls: ['./show-emp.component.css']
})
export class ShowEmpComponent implements OnInit {

  constructor(private service:SharedService) { }

  EmployeeList: any=[];
  ModalTitle: string | undefined;
  ActivateAddEditEmpComp: boolean = false;
  emp: any;


  ngOnInit(): void {
    this.refeshEmpList();
  }

  addClick(){
    this.emp={
      EmployeesId: 0,
      EmployeesName:"",
      Department:"",
      DateOfJoin: ""
    }

    this.ModalTitle = "Add Employee"; 
    this.ActivateAddEditEmpComp = true;
  }

  closeClick(){
    this.ActivateAddEditEmpComp = false;
    this.refeshEmpList();
  }

  editClick(item: any){
    this.ModalTitle = "Edit Employee";
    this.ActivateAddEditEmpComp = true; 
    this.emp = item
  }

  deleteClick(item :any){
    this.ActivateAddEditEmpComp = false;
    if(confirm('Are you sure ?')){
      this.service.deleteEmployee(item.EmployeesId).subscribe(data=>{
        alert(data.toString());
      });
    }
    this.refeshEmpList();
  }
  refeshEmpList(){
    this.service.getEmpList().subscribe(data=>{
      this.EmployeeList = data;
    });
  }
}
