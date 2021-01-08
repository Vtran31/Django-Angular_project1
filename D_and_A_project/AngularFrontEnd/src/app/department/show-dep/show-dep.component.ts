import { Component, OnInit } from '@angular/core';
import { SharedService } from 'src/app/shared.service'

@Component({
  selector: 'app-show-dep',
  templateUrl: './show-dep.component.html',
  styleUrls: ['./show-dep.component.css']
})
export class ShowDepComponent implements OnInit {

  constructor(private service:SharedService) { }

  DepartmentList: any=[];
  ModalTitle: string | undefined;
  ActivateAddEditDepComp: boolean = false;
  dep: any;



  ngOnInit(): void {
    this.refeshDepList();
  }

  addClick(){
    this.dep={
      DepartmentId: 0,
      DepartmentName:"",
    }

    this.ModalTitle = "Add Department"; 
    this.ActivateAddEditDepComp = true;
  }

  closeClick(){
    this.ActivateAddEditDepComp = false;
    this.refeshDepList();
  }

  editClick(item: any){
    this.ModalTitle = "Edit Department";
    this.ActivateAddEditDepComp = true; 
    this.dep = item
  }

  deleteClick(item :any){
    this.ActivateAddEditDepComp = false;
    if(confirm('Are you sure ?')){
      this.service.deleteDepartment(item.DepartmentId).subscribe(data=>{
        alert(data.toString());
      });
    }
    this.refeshDepList();
  }
  refeshDepList(){
    this.service.getDepList().subscribe(data=>{
      this.DepartmentList = data;
    });
  }

}
