package com.example.steps;

import io.cucumber.java.en.*;
import static org.junit.Assert.*;
import java.util.*;

public class Steps {
  private Map<String,String> users = new HashMap<>();
  private List<String> catalog = new ArrayList<>();
  private boolean dashboardVisible;
  private String lastError;
  private String query;

  @Given("existe una usuaria {string} con contraseña {string}")
  public void seedUser(String email, String pwd){
    users.put(email, pwd);
  }

  @When("inicio sesión con email {string} y contraseña {string}")
  public void login(String email, String pwd){
    if(!users.containsKey(email)) lastError="Usuario no existe";
    else if(!Objects.equals(users.get(email), pwd)) lastError="Credenciales inválidas";
    else dashboardVisible=true;
  }

  @Then("debo ver el panel principal")
  public void seeDashboard(){
    assertTrue(dashboardVisible);
  }

  @Then("debo ver el error {string}")
  public void seeError(String msg){
    assertEquals(msg, lastError);
  }

  @Given("el catálogo contiene:")
  public void seedCatalog(io.cucumber.datatable.DataTable table){
    catalog.clear();
    List<Map<String,String>> rows = table.asMaps(String.class, String.class);
    for(Map<String,String> row : rows){
      catalog.add(row.get("nombre"));
    }
  }

  @When("busco {string}")
  public void search(String q){
    this.query = q;
  }

  @Then("los resultados deben incluir {string}")
  public void resultsInclude(String name){
    assertTrue(catalog.contains(name));
  }

  @Then("veo el mensaje {string}")
  public void seeNoResults(String msg){
    if(query == null || !catalog.contains(query)){
      assertEquals("No se encontraron resultados", msg);
    } else {
      fail("Había resultados, no debería mostrarse el mensaje de 'No se encontraron resultados'.");
    }
  }
}
